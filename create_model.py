""" defines functions to train a model given a dataset. """

def create_model(dataset):
    model = initialize_model()
    model = train_model(model, dataset)
    return model

def initialize_model():
    
