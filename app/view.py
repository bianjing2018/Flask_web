from flask import Flask
from flask import render_template
from flask_login import LoginManager, LoginForm
app = Flask(__name__)
login_manger = LoginManager()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    pass