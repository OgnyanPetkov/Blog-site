from flask import Flask, render_template
import datetime
import requests
from post import Post

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
    return render_template("index.html", year=current_year, posts = post_objects)


@app.route("/blog/<int:index>")
def get_blog(index):
    current_year = datetime.datetime.now().year
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", year=current_year, post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
