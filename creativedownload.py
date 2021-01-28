import csv
import wget
import os
from cs50 import get_string

def main ():

    username = os.getlogin()
    download = get_string("file name: ")
    write = get_string("Folder Name for Desktop: ")



    with open(download, mode='r') as infile:
        reader = csv.DictReader(infile)

        folder = f'C:\\Users\\{username}\\Desktop\\{write}'
        if not os.path.exists(folder):
            os.makedirs(folder)

        for row in reader:
            #print(f"system curl {row['picture_link']} --output {row['picture_name']}")
            download = wget.download(row['picture_link'], f'{folder}/{row['picture_name']}')
            print ("%s downloaded!\n"%row['picture_name'])

    print("All Files Downloaded Successfully")

main()