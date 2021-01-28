# TODO
import sys
import csv
from cs50 import SQL

db = SQL("sqlite:///students.db")

def main():
    ## check command line for correct number of arguments (3)
    if len(sys.argv) != 2:
        print ("Incorrect command line arguments")
        sys.exit(1)
    else:
        print("Command Line Accepted")

    substring = ".csv"
    if substring not in sys.argv[1]:
        print("CSV needed as second arguemnt")
        sys.exit(1)
    else:
        print("Third is CSV")

    ## open the csv given by the command line argument
    infile = sys.argv[1]

    with open(infile, "r") as file:
    ## use CSV.reader or CSV.DictReader
        reader = csv.DictReader(file)

    ## for each row parse the name
    #use split method for parsing the names and make sure null for middle if it doesn't exist
        for row in reader:
            name = row["name"].split()
            birth = int(row["birth"])
            house = str(row["house"])

            if (len(name)) == 2:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?,?, ?, ?, ?)",
                name[0], None,name[1],house, birth)
            if (len(name)) == 3:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                    name[0],name[1],name[2],house,birth)



    ## insert each student into the students db
    ## use db.execute to insert into db



main()
