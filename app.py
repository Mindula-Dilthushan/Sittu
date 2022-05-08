# project name          : sittu application
# project contributions : chathumal/ ishanka/ mindula

from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

database = 'db/database.json'


# main root
@app.route('/')
def root():
    return render_template('index.html')


# check database.json file is empty
def empty_data(database):
    return os.path.exists(database) and os.stat(database).st_size == 0


# user save function
@app.route('/save', methods=["GET", "POST"])
def saveUser():
    userid = ''
    username = ''
    useramount = ''

    if request.method == "POST":
        if "userid" in request.form:
            userid = request.form["userid"]
        if "username" in request.form:
            username = request.form["username"]
        if "useramount" in request.form:
            useramount = request.form["useramount"]

    isEmpty = empty_data(database)

    if userid == '' or username == '' or useramount == '':
        pass
    else:
        if isEmpty:
            savedata = {
                           'id': userid,
                           'name': username,
                           'amount': useramount
                       },
            exit_file = open(database, "w")
            json.dump(savedata, exit_file, indent=3)
            exit_file.close()

        else:

            def saveJson(data, database='db/database.json'):
                with open(database, 'r+') as db:
                    json_data = json.load(db)
                    json_data.append(data)
                    db.seek(0)
                    json.dump(json_data, db, indent=3)

            savedata = {
                'id': userid,
                'name': username,
                'amount': useramount
            }

            saveJson(savedata)

    return render_template('adduser.html')


@app.route('/get_user', methods=["GET"])
def get_user():
    data = json.load(open(database, mode="r", encoding="utf-8"))
    new_data = jsonify(data)
    return new_data


@app.route('/test', methods=["GET"])
def test():
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
