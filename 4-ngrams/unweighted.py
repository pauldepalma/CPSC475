from random import choice, sample


def main():
  alph = [chr(i + 65) for i in range(0,26)]

  professions = ["scientist", "philosopher", "engineer", "priest"]
  print(choice(professions))

  levels = ["beginner", "intermediate", "advanced"]
  print(choice(levels))

  #one die
  die = choice(range(1,7))
  print("Die shows: " + str(die))

  #two dice
  dice = sample(range(1,7),2)
  print("Two dice show: " + str(dice))
  

main()

