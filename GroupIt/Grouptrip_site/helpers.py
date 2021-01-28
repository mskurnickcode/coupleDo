import os
import requests
import urllib.parse
import datetime

from cs50 import SQL
from flask import redirect, render_template, request, session
from functools import wraps

db = SQL("sqlite:///finance.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        response = requests.get(f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def get_data():
    user_id = session["user_id"]
    portfolio = get_portfolio(user_id)
    data = {
        'balance' : get_balance(user_id),
        'portfolio' : get_portfolio(user_id)
    }
    stocks = db.execute("SELECT * FROM user_stocks WHERE user_id = :user_id", user_id = user_id)
    data['current'] = current_price(stocks)
    return data





def get_portfolio(user_id):
    portfolio = db.execute("SELECT * FROM user_stocks WHERE user_id = :user_id GROUP BY ticker", user_id = user_id)
    return portfolio

def get_balance(user_id):
    balance = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id = user_id)
    return balance

def ownstock(stock, user_id):
    return db.execute("SELECT * FROM user_stocks WHERE user_id = :user_id AND ticker = :ticker AND quantity > 0",
    user_id = user_id, ticker = stock)

def buy_shares():

        stock = request.form.get("ticker")
        quantity = request.form.get("quantity")
        data = lookup(stock)
        if not data:
            return False

        user_id = session["user_id"]
        balance = get_balance(user_id)
        cost = data["price"] * int(quantity)

        ##update user stocks
        if (cost > balance[0]['cash']):
            return False

        if (int(quantity) < 1):
            return False

        if ownstock(stock, user_id):
            db.execute("UPDATE user_stocks SET quantity = quantity + :quantity WHERE user_id = :user_id AND ticker = :ticker",
            user_id = user_id, ticker = stock, quantity = quantity)
            return True

        else:
            db.execute("INSERT INTO user_stocks (user_id, ticker, price, quantity) VALUES (:user_id, :ticker, :price, :quantity);",
            user_id = session["user_id"], ticker = stock, price = data["price"], quantity = quantity)

            #insert into logs
            db.execute("INSERT INTO history (user_id, ticker, price, quantity, action, 'date_time') VALUES (:user_id, :ticker, :price, :quantity, :action, :date_time);",
            user_id = session["user_id"], ticker = stock, price = data["price"], quantity = quantity, action = '1', date_time = datetime.datetime.now())

            #update user balance
            db.execute("UPDATE users SET cash = (cash - :cost) WHERE id = :user_id", user_id = user_id, cost = cost)
            return True


def sell_shares():

        stock = request.form.get("stock")
        quantity = request.form.get("amount")
        data = lookup(stock)
        user_id = session["user_id"]
        portfolio = get_portfolio(user_id)
        cost = data["price"] * int(quantity)

        ##update user stocks
        owned = db.execute("SELECT SUM(quantity) AS shares FROM user_stocks WHERE quantity > 0 AND user_id = :user_id AND ticker = :stock GROUP BY ticker", user_id = user_id, stock = stock)
        if not owned:
            return False
        elif (int(quantity) > owned[0]['shares']):
            return False

        else:
            db.execute("UPDATE user_stocks SET quantity = quantity - :quantity WHERE user_id = :user_id AND ticker = :ticker",
            user_id = user_id, ticker = stock, quantity = quantity)
            print("Stocks sold")

            #insert into logs
            db.execute("INSERT INTO history (user_id, ticker, price, quantity, action, 'date_time') VALUES (:user_id, :ticker, :price, :quantity, :action, :date_time);",
            user_id = session["user_id"], ticker = stock, price = data["price"], quantity = quantity, action = '0', date_time = datetime.datetime.now())

            #update user balance
            db.execute("UPDATE users SET cash = (cash + :cost) WHERE id = :user_id", user_id = user_id, cost = cost)
            return True

def get_history(user_id):
    history = db.execute("SELECT * FROM history WHERE user_id = :user_id ORDER BY 'date_time'", user_id = user_id)
    for action in history:
        if action['action_id']:
            if action['action'] == 1:
                action['buy_sell'] = "Buy"
            elif action['action'] == 0:
                action['buy_sell'] = "Sell"
    return history

def current_price(stocks):
    for stock in stocks:
        if stock['ticker']:
            stock['current'] = lookup(stock['ticker'])['price']
        else:
            stock['current'] = 0
    return stocks
