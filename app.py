from flask import Flask, redirect, request, render_template, abort, flash, url_for, g
from user import User
from location import Location
import secrets
import sqlite3

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/")
def login_page():
    user_id = request.cookies.get('user_id')
    if (user_id):
        return redirect("/landmarker")
    return render_template("loginpage.html")

@app.route("/", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    users = get_users()
    for u in users:
        if (u.username == username and u.password == password):
            res = redirect("/landmarker")
            res.set_cookie('user_id', str(u.id),  max_age=3600)
            return res
    flash("Username or Password Invalid")
    return redirect("/")

@app.route("/landmarker")
def show_landmarker():
    user_id = request.cookies.get('user_id')
    if not (user_id):
        flash("Not logged in")
        return redirect("/")
    return render_template("index.html")

@app.route("/addlocation")
def add_location():
    user_id = request.cookies.get('user_id')
    if not (user_id):
        flash("Not logged in")
        return redirect("/")
    return render_template('location_form.html')

def get_users():
    allusers = get_db().execute("SELECT username, password, ID FROM users")
    lst = []
    for u in allusers:
        lst.append(User(u[0], u[1], u[2]))
    return lst

# database
def get_db():
    db = g.get("_database")
    if not db:
        g._database=sqlite3.connect("landmarker.db")
        db = g._database
    return db

@app.teardown_appcontext
def cleanup(exception):
    db = g.get("_database")
    if db:
        db.close()
