# project name : sittu application

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Welcome සීට්ටු Application !'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
