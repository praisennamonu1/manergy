from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manergy.db'
app.config['SECRET_KEY'] = '28d6afc0c91566bbefae52ba'

db = SQLAlchemy(app)
from manergy import routes