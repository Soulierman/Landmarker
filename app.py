from flask import Flask, redirect, request, render_template, abort, flash, url_for, g
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/addlocation")
def add_location():
    return render_template('location_form.html')
