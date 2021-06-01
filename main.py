from flask import Flask, render_template, request, redirect, url_for
import datetime
import requests
from post import Post
import smtplib
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, InputRequired

# Setting up your email and password to which people can send their messages. Best to submit them to environment.
USER_MAIL = "YOUR OWN EMAIL ADDRESS"
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

# Use the api.npoint to create your posts. Create a list with dictionary for each post. Each dictionary should
# contain the following keys: id, title, subtitle, body.
response = requests.get(url="https://api.npoint.io/056c133917b16793e561")  # Change the API to modify
blog_posts = response.json()
post_objects = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
current_year = datetime.datetime.now().year
app = Flask(__name__)
app.secret_key = "some secret string"


class LogForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[InputRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    message = TextAreaField(label="Message", validators=[InputRequired()])
    submit = SubmitField(label='Send')


@app.route('/')
def home():
    return render_template("index.html", year=current_year, posts=post_objects)


@app.route("/blog/<int:index>")
def get_blog(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", year=current_year, post=requested_post)


@app.route("/contact_me", methods=['GET', 'POST'])
def contact_me():
    contact_form = ContactForm()
    # If user submits data at this route.
    if contact_form.validate_on_submit():
        # send_email(contact_form.name, contact_form.email, contact_form.message)
        return render_template('contact_form.html', year=current_year, form=contact_form, msgsent=True)
    # If user requests the route.
    return render_template('contact_form.html', year=current_year, form=contact_form, msgsent=False)


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USER_MAIL, MAIL_PASSWORD)
        connection.sendmail(USER_MAIL, USER_MAIL, email_message)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LogForm()
    # If user submits data at this route.
    if login_form.validate_on_submit():
        return redirect(url_for('home'))

    # If user requests the route.
    return render_template('login.html', year=current_year, form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
