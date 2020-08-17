
#Numerical Python Course
#python-course.eu/weighted_choice_and_sample.php

import weighted_choice
from collections import Counter

def main():
    cities = ["New York",
              "LA",
              "Chicago",
              "Dallas",
              "Houston"]

    n = 10 #choices to make
    populations = [19,13,9,8,7] #in millions

    #compute the cumulative probabilities
    populations = weighted_choice.compute_weights(populations)
    
    #Make a list of n cities chosen in proportion to their weights
    outcomes = [weighted_choice.make_choice(cities, populations) for i in range(n)]

    #tot up the number of times each city was chosen
    ct = Counter(outcomes)

    for key in ct:
        print(str(key) + ": " + str(ct[key])) 

main()
