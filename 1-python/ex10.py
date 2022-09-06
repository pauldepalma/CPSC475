'''
Demonstrates:
   the use of command line arguments in a program invoked from the command line
   usage: python3 ex10.py 1 2 3 
'''

import sys


def main():
    n = len(sys.argv)  #number of arguments
    add = 0.0
    
    print(sys.argv[0])
    for i in range(1,n):
        add += float(sys.argv[i])

    print("sum is ",add)

main()
