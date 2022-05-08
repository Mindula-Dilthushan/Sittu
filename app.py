# project name          : sittu application
# project contributions : chathumal/ ishanka/ mindula

from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

database = 'db/database.json'


# main root
@app.route('/')
def root():
    return render_template('welcome.html')


# check database.json file is empty
def empty_data(database):
    return os.path.exists(database) and os.stat(database).st_size == 0


@app.route('/get_user')
def get_user():
    data = json.load(open(database, mode="r", encoding="utf-8"))
    # print(type(data))
    return data


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

    print("Save data ============================= ", userid, username, useramount)

    isEmpty = empty_data(database)

    if userid == '' or username == '' or useramount == '':
        print('userid : ', userid)
        print('username : ', username)
        print('useramount : ', useramount)

    else:
        print("data set")
        if isEmpty:
            print("data is empty ======================================")
            user_data = {
                'Users': [{
                    'id': userid,
                    'name': username,
                    'amount': useramount
                }],

            }
            exit_file = open(database, "w")
            json.dump(user_data, exit_file, indent=3)
            exit_file.close()
        else:
            print("data is not empty ===================================")

            def saveJson(data, database='db/database.json'):
                with open(database, 'r+') as db:
                    json_data = json.load(db)
                    json_data["Users"].append(data)
                    db.seek(0)
                    json.dump(json_data, db, indent=3)

            save_data = {
                'id': userid,
                'name': username,
                'amount': useramount
            }

            saveJson(save_data)

    return render_template('index.html')


@app.route('/debit', methods=["GET", "POST"])
def debit():
    return render_template('debit.html')


if __name__ == '__main__':
    app.run(debug=True)
