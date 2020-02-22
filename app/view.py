# @file :view.py

from flask import Flask, render_template, Blueprint, redirect, url_for, flash
from .Form import Login_Form, Register_Form
from .Model import Users
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from .run import app, LoginManager, db


@app.route('/')
def index():
    form = Login_Form()
    return render_template('login.html', form=form)


@app.route('/index')
def l_index():
    form = Login_Form()
    return render_template('login.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()
        if user is not None and user.pwd == form.pwd.data:
            logout_user(user)
            flash('登录成功')
            return render_template('home.html', name=form.name.data)
        else:
            flash('用户名或密码错误')
            return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录')
    return redirect(url_for('home.index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register_Form()
    if form.validate_on_submit():
        user = Users(name=form.name.data, pwd=form.pwd.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('home.index'))
    return render_template('register.html', form=form)