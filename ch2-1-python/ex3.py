'''
Demonstrates
    nested loops
    string concatenation
'''

def main():
    
    outer = int(input("Enter the outer value:  "))
    inner = int(input("Enter the inner value:  "))
    
    item = ''
    for i in range(outer):
        for j in range(inner):
            item = item + 'for '
            print (item)
        print()
        item = ''


    i = 0
    j = 0
    item = ''
    while (i < outer):
        while (j < inner):
            j += 1
            item = item + 'while '
            print (item)
        j = 0
        i += 1
        print()
        item = ''
main()
