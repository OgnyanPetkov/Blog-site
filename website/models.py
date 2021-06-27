from . import db
from flask_login import UserMixin


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    subtitle = db.Column(db.Text, unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.Text, nullable=False)
    length = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class User(db.Model, UserMixin):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    mail = db.Column(db.Text, unique=True, nullable=False)



