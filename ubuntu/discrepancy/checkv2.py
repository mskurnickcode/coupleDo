import csv
import pandas as pd
import glob
import datetime
from cs50 import get_string, get_int

file_location = {}
timestamp = datetime.datetime.today()
networks_data = {}
bidalgo_dict = {}

def main():
#get bidalgo file name
    bidalgo_csv = get_string("Bidalgo Data File:")

# get files to compare
    numberFiles = get_int("How many files: ")

    for files in range(numberFiles):
        file_location[files] = get_string(f"File {files} location: ")


#read bidalgo file name into csv
    with open(bidalgo_csv, mode='r') as infile:
        reader = pd.read_csv(infile)
        with open(f'Check_{timestamp}.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            bidalgo_dict = reader.filter(regex='Name|Spend|Cost')
            print(bidalgo_dict)


#read compare files into one dictionary
    for files in range(len(file_location)):
        with open(file_location[files], mode='r') as infile:
            reader = pd.read_csv(infile)
            reader_filtered = reader.filter(regex='Name|Spend|Cost')
            reader_filtered['Campaign Name'] = reader_filtered.pop('Name')
            print(reader_filtered)

    print(networks_data)

    match(bidalgo_dict, networks_data)

#compare dictionaries
def match(dictionary1, dictionary2):

    common_pairs = {}
    for key in dictionary1:
        if (key in dictionary2 and dictionary1[key] == dictionary2[key]):
            #Check if dictionaries share key
            common_pairs[key] = dictionary1[key]
    print(common_pairs)


main()