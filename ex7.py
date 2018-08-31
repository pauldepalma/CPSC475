'''
Demonstrates
    file operations: open, close, read entire file, read a line at a time
    testing for file existence
'''

def my_open():
    while(True):
        #be sure to place quotes around entry when you type it
        fin = input('Enter an input file name\n")
        try:
            fin = open(fin, 'r')
            break
        except:
            print("Invalid file name.  Try again.")
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
    read_file_as_string(fin)
    fin.close
    print('\n')
    fin = my_open()
    read_file_as_line(fin)
    fin.close()
    
    
    

main()

   

