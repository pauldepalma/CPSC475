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
    print fin
    print sys.argv[2]
    print sys.argv[3]
    stuff = sys.argv[3]
    print stuff[0]
    print stuff[1]
    print stuff[2]
    print result    #print the array
    print result[0]  #print the 0th row
    print result[1][3]  #print the cell in the 1st row 3rd col, .01
    
main()
