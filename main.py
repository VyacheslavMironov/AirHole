from flask import Flask, redirect, session, request, render_template, url_for
from models.db import *


app = Flask(__name__)


@app.route('/search/<str:name>', methods=["GET"])
def search(name):
    return searchCity(cityName=name)


@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        pass
    
    return render_template("index.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = userShow(email=request.form.get('email'), password=request.form.get('password'))
        if user:
            session['user'] = user

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
