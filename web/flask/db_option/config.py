#!/usr/bin/python
# -*- coding: utf-8 -*-
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABSE = 'db_name'
USERNAME = 'username'
PASSWORD = 'passwd'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABSE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

