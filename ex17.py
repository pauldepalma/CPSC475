'''
Demonstrates:
   Reading a CSV file into a numpy array
'''

import csv
import numpy
import sys


def main():
    fin = sys.argv[1]
    reader = csv.reader(open(fin, 'rb'), delimiter= ',')
    x = list(reader)
    result = numpy.array(x).astype('float')
    print result    #print the array
    print result[0]  #print the 0th row
    print result[1][3]  #print the cell in the 1st row 3rd col, .01
    
main()
