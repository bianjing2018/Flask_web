from flask import Flask
from flask_login import UserMixin
from run import db
from datetime import datetime


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    pwd = db.Column(db.String(1000))
    end_date = db.Column(db.DateTime)
    record_id = db.Column(db.Integer, db.ForeignKey('pay_record.id'))

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.end_date = datetime()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return 'User object: %s ' % self.name


class PayRecord(db.Model):
    __tablename__ = 'pay_record'

    id = db.Column(db.Integer, primary_key=True)
    pay_time = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    user = db.relationship('User', backref='users')


db.create_all()