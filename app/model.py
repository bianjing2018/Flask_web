from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from view import app
from flask_login import UserMixin
app.config.from_object('config')
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    super(UserMixin).get_id()
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(1000))
    end_date = db.Column(db.DateTime)
    record_id = db.Column(db.Integer, db.ForeignKey('pay_record.id'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return 'User object: %s ' % self.user_name


class PayRecord(db.Model):
    __tablename__ = 'pay_record'

    id = db.Column(db.Integer, primary_key=True)
    pay_time = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    user = db.relationship('User', backref='users')


db.create_all()