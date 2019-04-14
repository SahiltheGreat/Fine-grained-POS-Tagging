from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField

app = Flask(__name__)

app,config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mn

