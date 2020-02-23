from flask import Flask
from flask_login import UserMixin
from run import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    pwd = db.Column(db.String(255))
    end_date = db.Column(db.DateTime)
    record_id = db.Column(db.Integer, db.ForeignKey('pay_record.id'))

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = generate_password_hash(pwd)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    # 检查密码
    def check_password_hash(self, password):
        return check_password_hash(self.pwd, password)

    def __repr__(self):
        return 'User object: %s ' % self.name


class PayRecord(db.Model):
    __tablename__ = 'pay_record'

    id = db.Column(db.Integer, primary_key=True)
    pay_time = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    user = db.relationship('Users', backref='users')


db.create_all()