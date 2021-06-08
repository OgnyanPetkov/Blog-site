from flask import render_template, redirect, url_for, flash, Blueprint
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import User
from . import db
from . import current_year

auth = Blueprint('auth', __name__)


class LogForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


class SignUpForm(FlaskForm):
    name = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    confirm_pass = PasswordField(label="Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Up')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LogForm()
    # If user submits data at this route.
    if login_form.validate_on_submit():
        return redirect(url_for('views.home'))

    # If user requests the route.
    return render_template('login.html', year=current_year, form=login_form)


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignUpForm()
    mail = sign_up_form.email.data
    name = sign_up_form.name.data
    password = sign_up_form.password.data
    # If user submits data at this route.
    if sign_up_form.validate_on_submit():
        # Check if user exists
        user = User.query.filter_by(username=name).first()
        user_mail = User.query.filter_by(mail=mail).first()
        if user or user_mail:
            flash(message='Username or Email already in-use!')
            return render_template('sign_up.html', year=current_year, form=sign_up_form)
        else:
            hash_and_salt_pass = generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=8)
            new_user = User(username=sign_up_form.name.data, mail=sign_up_form.email.data, password=hash_and_salt_pass)
            db.session.add(new_user)
            db.session.commit
            return redirect(url_for('views.home'))

    # If user requests the route.
    return render_template('sign_up.html', year=current_year, form=sign_up_form)
