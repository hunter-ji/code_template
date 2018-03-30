#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('exmaple.db')
print ( "Opened database successfully!" )

conn.execute('''
create table users(
id integer primary key autoincrement,
username  char(11),
);''')

print ( "Table created successfully!" )
