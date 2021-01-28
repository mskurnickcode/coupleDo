import csv
from cs50 import get_string
from cs50 import SQL

def main ():

    download = get_string("CSV location: ")
    db = SQL("sqlite:///main.db")

    with open(download, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            country = row["name"]
            latitude = row["latitude"]
            longitude = row["longitude"]
            iso_country = row["country"]

            db.execute("CREATE TABLE IF NOT EXISTS countries (country TEXT, latitude REAL, longitude REAL, iso_country TEXT)")
            db.execute("INSERT INTO 'countries'('country', 'latitude', 'longitude', 'iso_country') VALUES(:country, :latitude, :longitude, :iso_country)",
                country = country, latitude = latitude, longitude = longitude, iso_country = iso_country)

    print("All countries entered successfully")

main()