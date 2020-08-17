
#Numerical Python Course
#python-course.eu/weighted_choice_and_sample.php
import numpy as np
from random import random

def compute_weights(weights):
    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()

    #transform weights to probabilities
    #numpy allows matrix multiplicaiton.  So here we normalizing the
    #the population or each city (in the city example) by normalizing
    #by the toltal population.  The output is list of probabilities
    np.multiply(weights, 1/sum_of_weights, weights)
    
    #transform the list of probabilities into a list of cumulative probabilities
    #this is the metaphorical sheet of paper discussed in class
    weights = weights.cumsum()
    return weights

#generate a random number
#traverse the cumulative probabilities looking for the first one greater than
#the random number generated
def make_choice(objects, weights):
    choice = random()
    for wtIdx in range(len(weights)):
      if choice < weights[wtIdx]:
         return objects[wtIdx]
    
