'''
  Demonstrates regular expressions in python.
  The directory holds 22 different regex patterns and corresponding strings
  patn and strn where n is the number, 'pat21' for example
'''

'''
  Puts braces around a string that matches the regex
  arg1: file containing regex
  arg2: file containing the string to be searched
  arg3: 'f' write output to reSub.txt. 's' write output to screen
  Usage:
    Bring up a python shell
    >>>from ex1 import reSub
    >>>reSub('pat1','str1', 'f')
    writes a file, reSub.txt, containing the string stored in str1 
    with all occurences of the regex in at1 marked.
'''
def reSub(patIn, strgIn, mode):
    import re
    strg = open(strgIn).read()
    pat = open(patIn).readline().strip()

    #Create a pattern object if you're going to do the same substitution
    #multiple times
    #MULTILINE tells ^ and $ to look at the beginnings and endings of all lines
    patObj = re.compile(pat,re.MULTILINE)
    strOut = patObj.sub('{\g<0>}',strg)  #\g<0> is the character group matched

    #not compiled version. produces same output as previous line
    #strOut = re.sub(pat,'{' + pat + '}',strg)  
    
    if mode == 'f':
        fout = open("reSub.txt","w")
        fout.write(strOut)
 
    if mode == 's':
            print(strOut)
            
    if mode != 'f' and mode != 's':
        print("3rd parameter must be 'f' or 's'")
    

'''
  Function that finds a regex pattern in a string and displays 
  one or all instances of the found pattern.
  arg1: regex pattern
  arg2: string
  arg3: 'A' for all occurrences, 'F' for the first occurrence
  Usage:
    Bring up a python shell
    >>>from ex12 import reFind
    >>>reFind('hello','hello world hello', 'F')
    displays 'hello' on the screen
    >>>reFind('hello','hello world hello', 'A')
    displays ['hello', 'hello'] on the screen
    
'''
def reFind(patIn,strgIn,mode):
    import re
    import sys
    if mode == 'A':
        m = re.findall(patIn,strgIn)
        if m:
            print(m)
            
    if mode == 'F':
        m = re.search(patIn,strgIn)
        if m:
            print(m.group())
            
    if mode != 'A' and mode != 'F':
        print("mode must be A (all) or F (first)")
        sys.exit()
        

