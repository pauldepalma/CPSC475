#a version of the classic eliza

import sys
import re
def doreply(instr):
    if re.search(r'^hello|hi$', instr):
        return 'Hi there!'
    if re.search('\W(hate|despise|loathe)|love\W', instr):
        return 'Wow! Those are some strong feelings you have! Tell me more...'
    if re.search("^(are|aren't|what|where|who|when|is|isn't|why|how)\W", instr):
        return 'good question!'
    return "So, tell me something about your mother."

def main():
    print ("Welcome! How may I help you? (type \"bye\" to quit.)\n")
    while True:
        instr = input("Patient: ")
        instr = instr.lower()
        if re.search('bye',instr):
            print("OK.  Until next time")
            return 0
        print (doreply(instr))
        print()
main()
