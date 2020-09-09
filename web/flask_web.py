import json

import pymysql
from flask import Flask, request

app = Flask(__name__)
app.debug = True


@app.route('/name')
def hello_world():
    d = {'name': '小红', 'age': 10, 'class': 'first'}
    return to_json(d)


@app.route('/url', methods=['GET', 'POST'])
def route_url():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode("utf-8"))
        _ = json_data.get("img_url")
        title = json_data.get("title")
        resp = {"response_code": 200, "title": title}
        return to_json(resp)


@app.route('/mysql', methods=['GET', 'POST'])
def route_get_mysql():
    conn = pymysql.connect(host='115.28.56.***', port=3306, user='root', password='12345678', db='student',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute('select person from t1 order by id asc')
    result = cur.fetchall()
    cur.close()
    conn.close()

    rlt = {}
    for i in result:
        for j in i:
            name = 'name%s' % j
            rlt[name] = j
    return to_json(rlt)


def to_json(content):
    return json.dumps(content, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
