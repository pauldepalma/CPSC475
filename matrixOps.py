'''
Useful matrix operations for minimum edit distance
Usage:
cs-student->python2.7
>>>from matrixOps import simpleOps
>>>simpleOps
'''


def simpleOps():
    import numpy as np

    #create an array and print it 
    num1 = np.matrix('1 2;3 4')
    print num1
    print

    #display the row 0 col 0
    print num1[0,0]
    print

    #display row 0
    print num1[0]
    print

    #display col 0
    print num1[:,0]
    print

    #create and display a 5X5 matrix of zeros
    num2 = np.zeros((5,5),dtype=np.int)
    print num2
    print

    #add 1 columnwise to the 0th row
    num2[0] = num2[0,:] + 1
    print num2

    #add 1 rowwise to the 0th column
    num2[:,0] = num2[:,0] + 1
    print num2
    print

    #create and display a 5X5 matrix of ones
    num3 = np.ones((5,5),dtype=np.int)
    print num3
    print

    #change the values in the 1st row to 0 .. through 4
    num3[1] = np.arange(0,5)
    print num3
    print

    #change the values in the 1st column to 0 through 4
    num3[:,0] = np.arange(0,5)
    print num3
    print

    #add 5 to the 2nd row 2nd col
    num3[2,2] += 5
    print num3
    print


    
    

    
    

    
                 
