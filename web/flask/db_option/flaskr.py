#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
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

@app.route('/')
def index():
    return 'Hello, World !'

if __name__ == '__main__':
    app.run(debug=True)

