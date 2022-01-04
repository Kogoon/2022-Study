from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'message': 'Hello World Web No.1'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
