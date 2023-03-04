from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("homepage.html")

@views.route("/login1")
def login1():
    return render_template("login1.html")

@views.route("/login2")
def login2():
    return render_template("login2.html")

@views.route("/signup1")
def signup1():
    return render_template("signup1.html")

@views.route("/signup2")
def signup2():
    return render_template("signup2.html")

@views.route("/signup3")
def signup3():
    return render_template("signup3.html")

@views.route("/forgot")
def signup4():
    return render_template("forgot.html")