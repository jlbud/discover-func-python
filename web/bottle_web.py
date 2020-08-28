import json

from bottle import route, run, template


@route('/name')
def nme_map():
    d = {'name': '小红', 'age': 10, 'class': 'first'}
    if 2 > 1:
        d['name'] = "小明"
        d['name2'] = "小果"
    return json.dumps(d, ensure_ascii=False)


@route('/name/<what>')
def name(what):
    return template('<b>Hello {{name}}</b>', name=what)


run(host='localhost', port=8080)
