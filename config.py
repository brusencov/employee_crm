from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URI = 'sqlite:///employees.db'
APP_SECRET = 'asdasdasdasd'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = APP_SECRET
db = SQLAlchemy(app)
