import csv
import wget
from cs50 import get_string

def main ():

    file = get_string("file name: ")


    with open(file, mode='r') as infile:
        #db.execute(f"CREATE TABLE bidalgo (campaignName varchar(255) NOT NULL, spend INT, impressions INT)")
        reader = csv.DictReader(infile)
        for row in reader:
            print(f"system curl {row['picture_link']} --output {row['picture_name']}")

            download = wget.download(row['picture_link'], stream = True)
            with open(row['picture_name'], 'wb') as f:
                for chunk in r:
                    f.write(chunk)

            print ("%s downloaded!\n"%row['picture_name'])

main()