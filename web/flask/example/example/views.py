# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template

from example import app, db
from example.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
