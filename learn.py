""" reads the data, creates and trains a model """

from read_data import read_data
from create_model import create_model
from test_model import test_model

dataset = read_data("train.csv")
model = create_model(dataset)
