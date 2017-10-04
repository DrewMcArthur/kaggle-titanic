""" defines functions that read data from a csv file, 
    and return the data in a numpy dataset              """

import csv

def read_data(filename):
    """ given a filename, open the file and read the information,
        format it, then return the data """
    print("Reading data from", filename)
    with open(filename) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        return data
