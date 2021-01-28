from flask import Flask, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///rankings.db")

@app.route("/", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("/index.html")
    else:
        name = request.form.get("name")
        score = request.form.get("score")
        db.execute("INSERT INTO rankings (name, score) VALUES (:name, :score)", name = name, score = score)
        return redirect("/leaderboard")

@app.route("/leaderboard")
def leaderboard ():
    leaders = db.execute("SELECT name, score FROM rankings ORDER BY score LIMIT 6")
    return render_template("leaderboard.html", leaders = leaders)


