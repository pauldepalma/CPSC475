

def do_stuff(inp):
    d = {}
    out = inp.split()
    for item in out:
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    return d


