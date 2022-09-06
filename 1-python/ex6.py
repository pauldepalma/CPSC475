'''
Demonstrates
    naive string search
    function use
'''
def searchSub(string,subStr,posStr_in):
    posSub = 0;
    posStr = posStr_in
    while(posSub < len(subStr)):
        if string[posStr] == subStr[posSub]:
            posSub = posSub + 1
            posStr = posStr + 1
        else:
            return -1
    return posStr_in

def findPos(string,subStr):
    posStr = 0
    lastSub = len(string) - len(subStr) #position of last possible substring

    while (posStr <= lastSub):
        pos = searchSub(string,subStr,posStr)
        if (pos >= 0):
            print ("substring starts at " + str(pos))
            break
        else:
            posStr = posStr + 1
    if posStr > lastSub:
        print ("substring not found")

def main():
    string = input("Enter a string\n")
    subStr = input("Enter a substring\n")
    findPos(string,subStr)
    
    

main()

   


