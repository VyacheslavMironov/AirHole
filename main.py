from flask import Flask, redirect, session, request, render_template, url_for
from models.db import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxx'


@app.route('/', methods=["POST", "GET"])
def main():
    lists = list()

    if request.method == "POST":
        data = searchCity(cityName=request.form.get('city'))
    else:
        data = allData()
    
    return render_template("index.html", data=data, count=len(data))


@app.route('/logout', methods=["POST", "GET"])
def logout():
    del session['user']
    return redirect(url_for('main'))


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = userShow(email=request.form.get('email'), password=request.form.get('password'))
        if user:
            session['user'] = user
            return redirect(url_for('main'))

    return render_template("login.html")


@app.route('/registration', methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        newUser(
            name=request.form.get('name'),
            surname=request.form.get('surname'),
            email=request.form.get('email'),
            password=request.form.get('password')
        )
        return redirect(url_for('login'))
    return render_template("registration.html")


if __name__ == '__main__':
    app.run()
