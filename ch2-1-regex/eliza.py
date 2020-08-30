import sys
import re
def doreply(instr):
    instr = instr.lower()
    if re.search(r'^hello|hi$', instr):
        return 'Hi there!'
    if re.search(r'\W(hate|despise|loathe)\W', instr):
        return 'Wow! Those are some strong feelings you have! Tell me more...'
    if re.search(r"^(are|aren't|what|where|who|when|is|isn't|why|how)\W", instr):
        return 'good question!'
    return "So, tell me something about your mother."
def main():
    print ("Welcome! How may I help you? (type \"bye\" to quit.)\n")
    while True:
        # Read user's input
        instr = input("Patient: ")
        instr = instr.lower()
        if re.search(r'\bbye\b', instr):
            print ("Nice chatting with you!\n")
            return 0
        print (doreply(instr))
        print()
if __name__ == "__main__":
    sys.exit(main())
