from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome සීට්ටු Application !'


if __name__ == '__main__':
    app.run()
