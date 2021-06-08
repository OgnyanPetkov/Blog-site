from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import datetime

current_year = datetime.datetime.now().year
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "some secret string"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
    app.config['SQLALCHEMY_BINDS'] = {'users': 'sqlite:///users.db'}
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .views import views as views_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(views_blueprint)
    from .models import User, Post
    db.create_all(app=app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
