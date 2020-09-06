'''
Demonstrates:
   the use of command line arguments
   usage: computer-science-> python ex10.py source target
'''

import sys


def main():
    for arg in sys.argv[1:]:
        print (arg) 

main()
