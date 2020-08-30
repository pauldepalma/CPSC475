'''
So much clearer without nested loops
'''
def for_loop(inner):
    item = ''
    for j in range(inner):
        item = item + 'for '
        print (item)

def while_loop(inner):
    item = ''
    j = 0
    while(j < inner):
        j += 1
        item = item + 'while '
        print (item)
        

    
def main():
    
    outer = int(input("Enter the outer value:  "))
    inner = int(input("Enter the inner value:  "))
    
    for i in range(outer):
        for_loop(inner)
        print()
        item = ''

    i = 0
    while (i < outer):
        while_loop(inner)
        i += 1
        print()
        item = ''
main()
