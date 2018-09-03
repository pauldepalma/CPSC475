'''
Demonstrates
    nested loops
    string concatenation
'''

def main():
    
    inner = int(raw_input("Enter the inner value:  "))
    outer = int(raw_input("Enter the outer value:  "))
    
    item = ''
    for i in range(inner):
        for j in range(outer):
            item = item + 'for '
            print (item)
        item = ''


    i = 0
    j = 0
    item = ''
    while (i < inner):
        while (j < outer):
            j += 1
            item = item + 'while '
            print (item)
        j = 0
        i += 1
        item = ''
main()
