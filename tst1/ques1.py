

def make_list(size):
    lst = []
    for i in range(size):
        lst.append(i)
    return lst    

def disp_list(lst):
    for item in lst:
        print (item)
            
def main():

    lst = make_list(5)
    disp_list(lst)

main()
    
