# project name : sittu application
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

database = "D:\MyWorksSpace\Python Projects\IJSE Workspace\Sittu\db\database.json"


@app.route('/hello')
def hello_world():
    return render_template('index.html')


def get_data():
    print("database :", database)


# @app.route('/')
# def main():
#     return render_template('index.html')

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0


@app.route('/', methods=["GET", "POST"])
def register():
    c_Id = ''
    name = ''
    amount = ''

    if request.method == "POST":
        if "c_Id" in request.form:
            c_Id = request.form["c_Id"]
        if "name" in request.form:
            name = request.form["name"]
        if "amount" in request.form:
            amount = request.form["amount"]

    is_empty = is_file_empty(database)

    if is_empty:
        dict1 = {
            'Users': [
                {'id': c_Id,
                 'name': name,
                 'Amount': amount,
                 },
            ]
        }
        out_file = open("db/database.json", "w")
        json.dump(dict1, out_file, indent=3)
        out_file.close()
    else:
        print('File is not empty')

        def write_json(new_data, filename='db/database.json'):

            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data["Users"].append(new_data)
                file.seek(0)

                json.dump(file_data, file, indent=3)

        y = {
            "id": c_Id,
            "name": name,
            "amonut": amount
        }

        write_json(y)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
