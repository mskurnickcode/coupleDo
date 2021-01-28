import csv
import wget
import os
from cs50 import get_string

def main ():

    username = os.getlogin()
    download = get_string("CSV location: ")
    write = get_string("Folder Name: ")



    with open(download, mode='r') as infile:
        reader = csv.DictReader(infile)

        if not os.path.exists(write):
            os.makedirs(write)

        for row in reader:
            dest_file = f"{write}/{row['picture_name']}.mp4"
            ##print(f"system curl {row['picture_link']} --output {row['picture_name']}")
            download = wget.download(row['picture_link'], dest_file)
            print ("%s downloaded!\n"%row['picture_name'])

    print("All Files Downloaded Successfully")

main()