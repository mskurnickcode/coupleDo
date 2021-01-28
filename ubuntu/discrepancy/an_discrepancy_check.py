import csv
import pandas as pd
import glob
import datetime
from cs50 import get_string, get_int

network_files = {}
df_arrays = {}
network_dict = {}
matches = 0
not_match = 0
match_dict = {}

def main():
    bidalgo_file = get_string("Bidalgo file location: ")

    network_number = get_int("How many ANs? ")

    for network in range(network_number):
        file_location = get_string("AN File: ")
        network_files[network] = file_location

    print(f"Bidalgo: {bidalgo_file}")
    for network in range(network_number):
        print(f"{network_files[network]}")


    columns = ["Campaign Name","Media Spend ($)"]
    bidalgo_df =  pd.read_csv(bidalgo_file, usecols=columns)
    bidalgo_dict = bidalgo_df.to_dict(orient = 'index')
    print(bidalgo_dict)


    ad_networks(network_number)
    #print(network_dict)

    #match(bidalgo_dict, network_dict)

    output = f"Bidalgo_Check_{datetime.datetime.today()}.csv"
    with open(output, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(bidalgo_dict.items())


def ad_networks(network_number):
    for network in range(network_number):
        df = pd.read_csv(network_files[network])
        df_arrays[network] = df.filter(regex='Name|Spend|Cost')
        df_arrays[network] = network_dict.update(df_arrays[network].to_dict())
    return network_dict




def match(dictionary1, dictionary2):
    common_pairs = {}
    for key in dictionary1:
        if (key in dictionary2 and dictionary1[key] == dictionary2[key]):
            #Check if dictionaries share key
            common_pairs[key] = dictionary1[key]
    print(common_pairs)



main()