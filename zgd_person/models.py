#!/user/bin/env python
# -*- conding:utf-8 -*-
# Author:zgd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///:memory:')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class USER(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(8),unique=True,nullable=False)
    pwd_hash = db.Column(db.String(255),nullable=False)
    #text = db.Column(db.Text)