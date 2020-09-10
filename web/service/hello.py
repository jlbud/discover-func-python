import json

from flask import request

from web.utils.json import to_json


def hello():
    d = {'name': '小红', 'age': 10, 'class': 'first'}
    return to_json(d)


def hello_url():
    resp = {"post": ""}
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode("utf-8"))
        _ = json_data.get("img_url")
        title = json_data.get("title")
        resp = {"response_code": 200, "title": title}
    return to_json(resp)
