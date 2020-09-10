from flask import Flask

from web.service.hello import hello_url, hello
from web.service.person import get_person

app = Flask(__name__)
app.debug = True


@app.route('/')
def root():
    return "404"


@app.route('/hello')
def hello_world():
    return hello()


@app.route('/hello_url', methods=['GET', 'POST'])
def route_url():
    return hello_url()


@app.route('/operate', methods=['GET', 'POST'])
def route_get_mysql():
    return get_person()


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
