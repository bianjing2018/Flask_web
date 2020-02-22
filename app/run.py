from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()


if __name__ == '__main__':
    app.run(port=9988)