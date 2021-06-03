from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import smtplib
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, InputRequired

# Setting up your email and password to which people can send their messages. Best to submit them to environment.
USER_MAIL = "YOUR OWN EMAIL ADDRESS"
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

current_year = datetime.datetime.now().year
app = Flask(__name__)
app.secret_key = "some secret string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    subtitle = db.Column(db.Text, unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.Text, nullable=False)
    length = db.Column(db.Text, nullable=False)


class BlogForm(FlaskForm):
    title = StringField(label='Title', validators=[InputRequired()])
    subtitle = StringField(label='Subtitle', validators=[InputRequired()])
    body = TextAreaField(label='Body', validators=[InputRequired()])
    difficulty = SelectField(label='Difficulty', choices=["🥾", "🥾🥾", "🥾🥾🥾", "🥾🥾🥾🥾", "🥾🥾🥾🥾🥾"])
    length = SelectField(label='Duration', choices=["⌛", "⌛⌛", "⌛⌛⌛", "⌛⌛⌛⌛", "⌛⌛⌛⌛⌛"])
    submit = SubmitField(label='Submit', validators=[InputRequired()])


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
    all_posts = Post.query.all()
    return render_template("index.html", year=current_year, posts=all_posts)


@app.route("/blog/<int:index>")
def get_blog(index):
    requested_post = None
    all_posts = Post.query.all()
    for post in all_posts:
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


@app.route("/add", methods=['GET', 'POST'])
def add_blog():
    blog = BlogForm()
    # If user submits data at this route.
    if blog.validate_on_submit():
        new_post = Post(title=blog.title.data, subtitle=blog.subtitle.data, body=blog.body.data,
                        difficulty=blog.difficulty.data, length=blog.length.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    # If user requests the route.
    return render_template('add.html', year=current_year, blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
