import numpy as np

def simple_ex(weights):
  
  #cWts = [0]+ list(np.cumsum(weights))
  cWts = list(np.cumsum(weights))
  print("weights")
  print(weights)
  print()

  print("cumulative weights")
  print(cWts)
  print()

  print("choose a random number, x, in the interval [0..1]")

  print("probability that x lies in the interval [0 .. cWts[0] = 1/5")               
  print("probability that x lies in the interval [cWts[0] .. cWts[1]] = 1/2")
  print("probability that x lies in the interval [cWts[1] .. cWts[2]] = 3/10")



def main():
  weights = [0.2, 0.5, 0.3]
  simple_ex(weights)

main()

