""" given a model, read test data, test the model, return accuracy """

from read_data import read_data

def test_model(model):
    dataset = read_data("test.csv")
    return get_accuracy(model, dataset)

def get_accuracy(model, dataset):
    """ return percent accuracy of the model on test data """
    i, o = dataset
    preds = model.predict(i)
    return accuracy_score(o, preds)
