import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import *

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    portfolio = get_portfolio(user_id)
    balance = get_balance(user_id)
    current = current_price(portfolio)
    data = get_data()

    cash = balance[0]['cash']
    return render_template("homepage.html", data = data, cash = cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("ticker") or not request.form.get("quantity"):
            return apology("Must Provide a Stock and Quantity", 403)

        if buy_shares() == True:
            return redirect("/")
        else:
            return apology("Not enough cash or incorrect quantity", 403)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]
    history = get_history(user_id)
    balance = get_balance(user_id)

    cash = int(balance[0]['cash'])

    """Show history of transactions"""
    return render_template("history.html", history = history, cash = cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("ticker"):
            return apology("Must Provide a Stock", 403)
        else:
            stock = request.form.get("ticker")
            data = lookup(stock)
            return render_template("quoted.html", data = data)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("login_username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not ((request.form.get("login_password")) == (request.form.get("password_check"))):
            return apology("must provide passwords that match", 403)

        # register in DB
        username = request.form.get("login_username")
        check_unique = db.execute("SELECT username FROM users WHERE username = :username", username = username)
        if check_unique:
            return apology("That usernameis taken. Please try a new one", 403)

        pre_hashed_password = request.form.get("login_password")
        hashed = generate_password_hash(pre_hashed_password, method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username = username, hash = hashed)

        # Redirect user to home page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        if not request.form.get("stock") or not request.form.get("amount"):
            return apology("Must Provide a Stock and Quantity", 403)
        if sell_shares() == True:
            return redirect("/")
        else:
            return apology("Not enough shares", 403)
    else:
        user_id = session["user_id"]
        portfolio = get_data()
        return render_template("sell.html", portfolio = portfolio)


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        user_id = session["user_id"]
        username = db.execute("SELECT * FROM users WHERE id = :user_id",
                          user_id=user_id)

        # Ensure username exists and password is correct
        if not check_password_hash(username[0]["hash"], request.form.get("current")):
            return apology("Current Password Incorrect", 403)

        if not (request.form.get("new_password1") == request.form.get("new_password2")):
            return apology("New Passwords Don't Match")

        hashed = generate_password_hash(request.form.get("new_password2"), method='pbkdf2:sha256', salt_length=8)
        db.execute("UPDATE users SET hash = :hash WHERE id = :user_id",
            user_id = user_id, hash = hashed)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        user_id = session["user_id"]
        username = db.execute("SELECT username FROM users WHERE id = :user_id",
                          user_id=user_id)
        return render_template("change_password.html", username = username)



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)