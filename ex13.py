'''
Demonstrates:
    Plotting a function
    For now, this requires python 3
'''

import matplotlib.pyplot as plt


def main():
    x = [i for i in range(0,10)]
    y = [i**2 for i in x]
    plt.plot(x,y)
    plt.show()
    
main()
    
