# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('example')
app.config.from_pyfile('config.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from example import views, errors, commands
