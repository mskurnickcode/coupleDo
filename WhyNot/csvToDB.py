import csv
from cs50 import get_string
from cs50 import SQL

def main ():

    download = get_string("CSV location: ")
    db = SQL("sqlite:///main.db")

    with open(download, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            country = row["Country or territory"]
            currency = row["Currency"]
            currency_code = row["ISO-4217"]


            db.execute("CREATE TABLE IF NOT EXISTS currencys (country TEXT, currency TEXT, currency_code TEXT)")
            db.execute("INSERT INTO currencys ('country', 'currency', 'currency_code') VALUES (:country, :currency, :currency_code)",
                country = country, currency = currency, currency_code = currency_code)

    print("All currencys entered successfully")

main()