
#Numerical Python Course
#python-course.eu/weighted_choice_and_sample.php

#Simulation of weighted dice.

from collections import Counter

import weighted_choice

def main():

    #Die has six sides, each has probability of occurring = 1/6
    die = [1,2,3,4,5,6]

    #Now weight the die so that 1 has p = 1/12, 2 has p = 2/12 ...
    weights = [1/12,1/6,1/6,1/6,1/6,3/12]

    #toss the die n times
    n = 1000  

    #compute the cumulative probabilities
    weights = weighted_choice.compute_weights(weights)

    #list of n faces (e.g.1 through 6) as they appear
    outcomes = [weighted_choice.make_choice(die,weights) for i in range(n)]

    #tot up the number of appearances for each face
    ct = Counter(outcomes) #dict key = die face value
                           #value = num occurrences for a given face

    
    
    #display number of appearances for each face along with the fraction of the total
    for face in die:
        print("Face " + str(face) + "\t " + str(ct[face]) + "\t" + " (" + str(ct[face]/n) + ")")


main()
