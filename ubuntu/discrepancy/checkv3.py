import csv
import datetime
import pandas as pd
from cs50 import SQL, get_string, get_int

file_location = {}
timestamp = datetime.datetime.today()
db = SQL("sqlite:///check.db")

def main():
#get bidalgo file name
    bidalgo_csv = input("Bidalgo Data File: ")

# get files to compare
    numberFiles = get_int("How many files: ")

    for files in range(numberFiles):
        file_location[files] = input(f"File {files} location: ")


#read bidalgo file name into csv
    with open(bidalgo_csv, mode='r') as infile:
        #db.execute(f"CREATE TABLE bidalgo (campaignName varchar(255) NOT NULL, spend INT, impressions INT)")
        reader = csv.DictReader(infile)
        for row in reader:
            campaignName = row["Campaign Name"]
            spend = row["Media Spend ($)"]
            impressions = row["Impressions"]

            db.execute("INSERT INTO bidalgo (campaignName, spend, impressions) VALUES(?,?, ?)",
                campaignName, spend, impressions)
                
    print("Bidalgo inserted successfully")


#read compare files into one dictionary
    for files in range(len(file_location)):
        db.execute(f"CREATE TABLE {file_location[files]} (campaignName varchar(255) NOT NULL, spend INT, impressions INT)")
        with open(file_location[files], mode='r') as infile:
            reader = csv.DictReader(infile)
            
            for row in reader:
                campaignName = row["Name"]
                spend = row["Spend"]
                impressions = row["Impressions"]

                db.execute("INSERT INTO bidalgo (campaignName, spend, impressions) VALUES(?,?, ?)",
                campaignName, spend, impressions)
        print(f"{file_location[files]} inserted successfully")
main()