#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, send_from_directory

UPLOAD_FOLDER = "/web/uploads"
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename, as_attachment=True)
