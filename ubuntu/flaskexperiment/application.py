from flask import Flask, redirect, render_template, request

app = Flask(__name__)

strings = []

@app.route("/")
def string ():
    return render_template("strings.html", strings = strings)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        string = request.form.get("comment")
        strings.append(string)
        return redirect("/")
