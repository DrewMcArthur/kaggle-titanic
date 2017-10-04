""" defines functions to train a model given a dataset. """

from sklearn.neuralnetwork import MLPClassifier

def striptotitle(Xs):
    for x in Xs:
        x[3] = x[3].split(' ')[1]
    return Xs

def create_model(dataset):
    model = initialize_model()
    
    model.fit(dataset)
    return model

def initialize_model():
    """ initializes the model using sklearn objects """
    # create objects
    titleStripper = FunctionTransformer(striptotitle)

    # neural net.  needs: 
    #  number of hidden layers and number of neurons in each layer
    estimator = MLPClassifier()

    # create pipeline TODO: add objects to argument list
    return make_pipeline(titleStripper, estimator)   
