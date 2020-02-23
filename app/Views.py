# @file :view.py

from flask import Flask, render_template, Blueprint, redirect, url_for, flash
from Form import Login_Form, Register_Form
from Model import Users
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from run import app, LoginManager, db
from flask_cors import CORS
CORS(app)


@app.route('/')
def index():
    form = Login_Form()
    # return render_template('login.html', form=form)
    return render_template('ssx_login.html', form=form)


@app.route('/index')
def l_index():
    form = Login_Form()
    return render_template('ssx_login.html', form=form)


@app.route('/ssx_home')
def ssx_home():
    form = Login_Form()
    return render_template('ssx_home.html', form=form)


@app.route('/ssx_download')
def ssx_download():
    form = Login_Form()
    return render_template('ssx_download.html', form=form)


@app.route('/ssx_introduction')
def ssx_introduction():
    form = Login_Form()
    return render_template('ssx_introduction.html', form=form)


@app.route('/ssx_help')
def ssx_help():
    form = Login_Form()
    return render_template('ssx_help.html', form=form)


@app.route('/ssx_contact')
def ssx_contact():
    form = Login_Form()
    return render_template('ssx_contact.html', form=form)


@app.route('/ssx_account_info')
def ssx_account_info():
    form = Login_Form()
    return render_template('ssx_account_info.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()
        if user is not None and user.check_password_hash(form.pwd.data):
            login_user(user)
            flash('登录成功')
            return render_template('ssx_home.html', name=form.name.data)
        else:
            flash('用户名或密码错误')
            return render_template('ssx_login.html', form=form)
    return render_template('ssx_login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register_Form()
    if form.validate_on_submit():
        if form.pwd.data != form.confirm_pwd.data:
            flash('两次密码输入不一致')
            return render_template('ssx_register.html', form=form)
        if Users.query.filter_by(name=form.name.data).first():
            flash('登录名已存在')
            return render_template('ssx_register.html', form=form)
        user = Users(name=form.name.data, pwd=form.pwd.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('login'))
    return render_template('ssx_register.html', form=form)