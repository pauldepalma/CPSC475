'''
Demonstrates:
    regular expressions
'''    
import re
def find(pattern,inString):
    m = re.search(pattern,inString)
    if m:
        print (m.group())
    
    
