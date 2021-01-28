# TODO
import sys
import csv
from cs50 import SQL

db = SQL("sqlite:///students.db")

def main():
    if (len(sys.argv) != 2):
        print("Error: Incorrect number of command line arguments")
        sys.exit(1)

    #if sys.argv[1] != ("Ravenclaw" or "Gryffindor" or "Slytherin" or "Hufflepuff"):
     #   print("Error: Inputted house doesn't exist")
      #  sys.exit(2)

    house = sys.argv[1]
    data = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house = '{house}' ORDER BY last ASC, first ASC;")
    for row in data:
        if row["middle"] != None:
            print(row["first"]," ", row["middle"], " ", row["last"],", born ",row["birth"], sep='')
        else:
            print(row["first"]," ",row["last"], ", born ", row["birth"], sep='')



main()
