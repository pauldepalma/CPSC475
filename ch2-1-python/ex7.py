'''
Demonstrates
    file operations: open, close, read entire file, read a line at a time
    testing for file existence
    try..catch block
'''

import sys

def my_open():
    while(True):
        fin = input('Enter an input file name\n')
        try:
            fin = open(fin, 'r')
            break
        except:
            print("file does not exist  Try again.")
    return fin

def read_file_as_string(fin):
    string = fin.read()
    print (string)

def read_file_as_line(fin):
    for line in fin:
        print(line.rstrip('\n')) #rstrip removes '\n' from each line because
                                 #print inserts '\n'


def main():
    fin = my_open()
    read_mode = input("Read as string or line (S/L)?\n")
    if (read_mode == 'S'):
        read_file_as_string(fin)
    else:
        if (read_mode == 'L'):
            read_file_as_line(fin)
        else:
            print("Invalid read mode")
            sys.exit()  #end execution
    fin.close()
    print('\n')
    

main()

   


