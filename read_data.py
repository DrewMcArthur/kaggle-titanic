""" defines functions that read data from a csv file, 
    and return the data in a numpy dataset              """

import pandas as pd

def read_data(filename):
    """ given a filename, open the file and read the information,
        format it, then return the data """
    print("Reading data from", filename)
    return pd.read_csv(filename)
