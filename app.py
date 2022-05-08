# project name          : sittu application
# project contributions : chathumal/ ishanka/ mindula

import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

database = "D:\MyWorksSpace\Python Projects\IJSE Workspace\Sittu\db\database.json"


@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
