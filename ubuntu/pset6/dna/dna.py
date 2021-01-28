import sys
import csv
import re
import pandas as pd
from collections import defaultdict
from cs50 import get_string

def main():
    #check that there is the right number of arguments
    if len(sys.argv) != 3:
        print("Incorrect Number of Inputs")
        sys.exit(1)

    #if len(sys.argv) == 3:
    #    print("Successful number of arguments")

    #check that arguments were stored
    #print('Number of arguments:', len(sys.argv), 'arguments.')
    #print('Argument List:', str(sys.argv))

    sequences = {}
    
    #open arguments into stored memory
    with open(sys.argv[1]) as database:
        database_contents = csv.DictReader(database)
        field_names = database_contents.fieldnames
        for row in database_contents:
            people = row
            break
        
    for item in people:
        sequences[item] = 1

    with open(sys.argv[2]) as strand:
        strand_contents = strand.read()


    #find string length
    strand_length = len(strand_contents)

    #find AGATC,AATG,TATC
    strands = {}
    strand_count = {}
    for column in range(0,len(field_names)):
        strands[column] = max(re.findall('((?:' + re.escape(field_names[column]) + ')*)', strand_contents), key = len)
        count = (len(strands[column])/len(field_names[column])) - 1
        sequences[field_names[column]] += count
    
    del sequences['name']
    #print(f"{sequences}")
    
    with open(sys.argv[1], newline='') as database_match:
        people_list = csv.DictReader(database_match)
        for person in people_list:
            match = 0
    
            for dna in sequences:
                if sequences[dna] == int(person[dna]):
                    match += 1
            
            if match == len(sequences):
                print(person['name'])
                exit()

    print("No match")
        
    
    







main()