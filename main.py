from flask import Flask, render_template, request
import datetime
import requests
from post import Post
import smtplib
import os

# Setting up your email and password to which people can send their messages. Best to submit them to environment.
USER_MAIL = "YOUR OWN EMAIL ADDRESS"
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

# Use the api.npoint to create your posts. Create a list with dictionary for each post. Each dictionary should
# contain the following keys: id, title, subtitle, body.
response = requests.get(url="https://api.npoint.io/056c133917b16793e561")
blog_posts = response.json()
post_objects = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year, posts=post_objects)


@app.route("/blog/<int:index>")
def get_blog(index):
    current_year = datetime.datetime.now().year
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", year=current_year, post=requested_post)


@app.route("/contact_me", methods=['GET', 'POST'])
def contact_me():
    current_year = datetime.datetime.now().year
    if request.method == 'POST':
        current_year = datetime.datetime.now().year
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(name, email, message)
        return render_template('contact_form.html', year=current_year, msgsent=True)
    return render_template('contact_form.html', year=current_year, msgsent=False)


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USER_MAIL, MAIL_PASSWORD)
        connection.sendmail(USER_MAIL, USER_MAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
