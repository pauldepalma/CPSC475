'''
Demonstrates:
   Reading a CSV file into a numpy array using comman line arguments
   ->python ex15.py matA.csv
   
'''

from numpy import genfromtxt
import sys


def main():
    fin = sys.argv[1]
    result = genfromtxt(fin,delimiter=',')
    
    print (fin)
    print (result)    #print the array
    print (result[0])  #print the 0th row
    print (result[1][3])  #print the cell in the 1st row 3rd col, .01
   
    
main()
