'''
Demonstrates:
   finding all regular expression patterns in a file 
'''    
import re
def find(pattern,file):   #surround input file with single quotes when entering
    f = open(file,'r') 
    strings = re.findall(pattern,f.read())
    print strings 
