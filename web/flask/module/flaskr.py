#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash, json, jsonify, session
from exts import db
import config
from models import Article

# init
# migrate
# upgrade
# 模型 -> 迁移文件 -> 表

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

#  @app.before_request
#  def before_request():
#      pass

# ajax
# data = request.get_data()
# op = json.loads(data)["op"]

@app.route('/')
def index():
    return 'Hello, World !'

@app.route("/login/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        db_passwd = User.query.filter(User.username == username).first()
        if not db_passwd:
            error = 'Invalid username'
        elif password != db_passwd.password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

#　登出
@app.route("/logout")
def logout():
    if not session.get('logged_in'):
        return redirect("login")
    session.pop('logged_in', None)
    session.pop('username')
    return redirect(url_for('index'))

# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
