'''
  Demonstrates regular expressions in python.  I've repackaged the three
  techniques demonstrated in class as functions
'''

'''
  Function that marks strings found with a regular expression, writing the
  output to re_show.txt 
  arg1 is the pattern to be matched
  arg2 is either the name of the file containing the string that is to be
    searched or the string itself
  arg3 is 'f' if arg2 is a file name
  arg4 is the number of matches to find. '0' finds all matches
  Usage:
    Bring up a python shell
    >>>from ex14 import reShow
    >>>re_show('pat1','str1', 'f', 0)
    writes a file, reShow.txt, containing the string stored str1 
    with all occurences of the regex pat1 marked.

    >>>re_show.py('a',"Mary Ann stopped by Mona's",'s' 1)
    displays the input string with the first instance of 'a' marked
'''

def reShow(patIn, strgIn, mode,times):
    import re
    if mode == 'f':
        strg = open(strgIn).read()
        pat = open(patIn).readline().strip()
    else:
        strg = strgIn
        pat = patIn
    patObj = re.compile(pat)

    #this curious syntax surrounds the pattern found by braces
    #notice that the sub function can be repurposed
    if (times > 0):
        strOut = patObj.sub("{\g<0>}",strg,times)
    else:
        strOut = patObj.sub("{\g<0>}",strg)

    if mode == 'f':
        fout = open("reShow.txt","w")
        fout.write(strOut)
    else:
        print strOut

'''
  Function that finds a regex pattern in a string and displays the first
  instance of the found pattern
  Function that finds a regex pattern in a string and displays 
  all instances of the found pattern if mode is 'A' otherwise
  displays only the first instance 
'''
def reFind(pattern,strgIn,mode):
    import re
    if mode == 'A':
        m = re.findall(pattern,strgIn)
    else:
        m = re.search(pattern,strgIn)
    if m:
        return m
    else:
        print "No Match"


