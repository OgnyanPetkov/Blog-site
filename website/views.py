from flask import render_template, redirect, url_for, flash, Blueprint
import smtplib
from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from .models import Post
from . import db
from . import current_year

views = Blueprint('views', __name__)


class BlogForm(FlaskForm):
    title = StringField(label='Title', validators=[InputRequired()])
    subtitle = StringField(label='Subtitle', validators=[InputRequired()])
    body = TextAreaField(label='Body', validators=[InputRequired()])
    difficulty = SelectField(label='Difficulty', choices=["🥾", "🥾🥾", "🥾🥾🥾", "🥾🥾🥾🥾", "🥾🥾🥾🥾🥾"])
    length = SelectField(label='Duration', choices=["⌛", "⌛⌛", "⌛⌛⌛", "⌛⌛⌛⌛", "⌛⌛⌛⌛⌛"])
    submit = SubmitField(label='Submit', validators=[InputRequired()])


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[InputRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    message = TextAreaField(label="Message", validators=[InputRequired()])
    submit = SubmitField(label='Send')


@views.route('/')
def home():
    all_posts = Post.query.all()
    return render_template("index.html", year=current_year, posts=all_posts)


@views.route("/blog/<int:index>")
def get_blog(index):
    requested_post = None
    all_posts = Post.query.all()
    for post in all_posts:
        if post.id == index:
            requested_post = post
    return render_template("post.html", year=current_year, post=requested_post)


@views.route("/contact_me", methods=['GET', 'POST'])
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


@views.route("/add", methods=['GET', 'POST'])
@login_required
def add_blog():
    blog = BlogForm()
    # If user submits data at this route.
    if blog.validate_on_submit():
        new_post = Post(title=blog.title.data, subtitle=blog.subtitle.data, body=blog.body.data,
                        difficulty=blog.difficulty.data, length=blog.length.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('views.home'))

    # If user requests the route.
    return render_template('add.html', year=current_year, blog=blog)
