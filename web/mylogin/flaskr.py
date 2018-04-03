#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash, json, jsonify, session
import os

SECRET_KEY = os.urandom(24)

app = Flask(__name__)
app.config.from_object(__name__)

# 登录
@app.route("/login/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        print (username, password)
        cur = g.db.execute("select username from users")    
        usernames = [row[0] for row in cur.fetchall()]
        cur2 = g.db.execute("select password from users where username = ?",[username])
        the_password = [row[0] for row in cur2.fetchall()][0]
        if username not in usernames:
            error = 'Invalid username'
        elif password != the_password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

#　登出
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
