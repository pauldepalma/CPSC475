'''
Demonstrates:
   the use of command line arguments in a program invoked from the command line
   usage: python3 ex10.py source target
'''

import sys


def main():
    for arg in sys.argv[1:]:
        print (arg) 

main()
