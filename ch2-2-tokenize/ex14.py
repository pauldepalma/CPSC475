'''
Demonstrates:
    Plotting a function with matplotlib
    Install matplotlib from the command line using pip (pip is package manager for
    python)

To install matlib, bring up a terminal window

    python-m pip install --upgrade pip
    python -m pip install -U matplotlib
'''

import matplotlib.pyplot as plt


def main():
    x = [i for i in range(0,100)]
    y = [i**2 for i in x]
    plt.plot(x,y)
    plt.show()
    
main()
    
