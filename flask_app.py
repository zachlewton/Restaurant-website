
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")



@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")