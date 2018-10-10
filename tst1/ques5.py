

def reFind(pattern,strgIn,mode):
    import re
    if mode == 'A':
        m = re.findall(pattern,strgIn)
        return m
    else:
        m = re.search(pattern,strgIn)
        return m.group()
    else:
        print "No Match"


