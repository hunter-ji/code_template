#!/usr/bin/python
# -*- coding: utf-8 -*-
@app.route("/table", methods=["GET", "POST"])
def table():
    data = [
            {
                "id": "0",
                "sid": "15080930211",
                "name": "kuari",
                "details": "details"
                }
    ]
    return jsonify(data)

