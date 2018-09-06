'''
Demonstrates:
   finding all regular expression patterns in a file 
'''    
import re
#surround pattern and file with single quotes
def find(pattern,file): 
    f = open(file,'r') 
    strings = re.findall(pattern,f.read())
    print strings 
