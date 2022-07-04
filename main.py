from flask import Flask, session, request, render_template
from models.db import *


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
@app.route('/search', methods=["POST", "GET"])
def main():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/registration', methods=["POST", "GET"])
def registration():
    return render_template("registration.html")


if __name__ == '__main__':
    app.run()
