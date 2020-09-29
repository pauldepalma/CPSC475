
import numpy as np
from random import random

def compute_weights(weights):
    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()

    #transform weights to probabilities
    #numpy allows matrix multiplicaiton.  So here we are normalizing the
    #the population of each city (in the city example) by dividing by
    #the total population.  The output is a list of probabilities
    np.multiply(weights, 1/sum_of_weights, weights)
    
    #transform the list of probabilities into a list of cumulative probabilities
    #this is the metaphorical sheet of paper discussed in class
    weights = weights.cumsum()
    return weights

#generate a random number
#traverse the cumulative probabilities looking for the first one greater than
#the random number generated
#in the city example, object is a city, weight is a population
def make_choice(object, weight):
    choice = random()
    for wtIdx in range(len(weight)):
      if choice < weight[wtIdx]:
         return object[wtIdx]
    
