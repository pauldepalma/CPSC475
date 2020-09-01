'''
Demonstrates:
    list structure
    tuple structure
    functions returning > 1 variable
    an approach to error checking
    list comprehension
'''

import random

LOW = 1
HIGH = 100

def make_list(size):
    '''
    #An obvious way
    lst = []
    for i in range(size):
        lst.append(random.randint(LOW,HIGH))
    return lst
    '''
    #A more pythonic way. called a "list comprehension"
    #not the set builder constuction
    return [random.randint(LOW,HIGH) for i in range(size)]
    


def get_data():
    while(True):
        size = int(input("How many items should I put in the list?  \n"))
        if size < 1:
            print("Number of items must exceed 0.  Try again.")
        else:
            break

    while(True):
        direction = input("Print top to bottom or bottom to top (T/B on VM, 'T'/'B' on grace)?  \n")
        if direction not in ('T','B'):
            print("Direction must be T or B.  Try again.")
        else:
            break

    return size, direction
    

def disp_list(lst,direction):
    lst.sort()  #sorts the list.  Isn't Python great
    if direction == 'T':
        for item in lst:  #a very common Python construction
            print(item)
    
    if direction == 'B':
        i = len(lst) -1
        while (i >= 0):
            print(lst[i])
            i -= 1
            
    
def main():
    size, direction = get_data() #return more than 1 value
    lst = make_list(size)
    disp_list(lst,direction)

main()
    
