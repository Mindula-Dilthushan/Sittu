# project name          : sittu application
# project contributions : chathumal/ ishanka/ mindula

from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

userdb = 'db/userdb.json'


# main root
@app.route('/')
def root():
    return render_template('index.html')


# check userdb.json file is empty
def empty_data(userdb):
    return os.path.exists(userdb) and os.stat(userdb).st_size == 0


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

    isEmpty = empty_data(userdb)

    if userid == '' or username == '' or useramount == '':
        pass
    else:
        if isEmpty:
            savedata = {
                           'id': userid,
                           'name': username,
                           'amount': useramount
                       },
            exit_file = open(userdb, "w")
            json.dump(savedata, exit_file, indent=3)
            exit_file.close()

        else:

            def saveJson(data, userdb='db/userdb.json'):
                with open(userdb, 'r+') as db:
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


@app.route('/get_all_user', methods=["GET"])
def get_all_user():
    data = json.load(open(userdb, mode="r", encoding="UTF-8"))
    new_data = jsonify(data)
    return new_data


@app.route('/loan', methods=["GET", "POST"])
def loan():
    return render_template('loan.html')


@app.route('/get_user', methods=["GET"])
def get_user():
    return jsonify(json.load(open(userdb, mode="r", encoding="UTF-8")))


@app.route('/confirm_users', methods=["GET", "POST"])
def confirm_users():
    userAmount_2 = 0
    userAmount_3 = 0
    usersAmoutTot = 0
    loanMax = 0
    userId_1_B = 0
    userId_2_B = 0

    if request.method == "POST":
        if "userAmount_2" in request.form:
            userAmount_2 = request.form["userAmount_2"]
        if "userAmount_3" in request.form:
            userAmount_3 = request.form["userAmount_3"]
            usersAmoutTot = float(userAmount_2) + float(userAmount_3)
            loanMax = float(usersAmoutTot) / 100 * 80
            userId_1_B = userAmount_2
            userId_2_B = userAmount_3

    return render_template(
        'loan.html',
        userAmount_2=userAmount_2,
        userAmount_3=userAmount_3,
        usersAmoutTot=usersAmoutTot,
        loanMax=loanMax,
        userId_1_B=userId_1_B,
        userId_2_B=userId_2_B
    )


@app.route('/test')
def test():
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
