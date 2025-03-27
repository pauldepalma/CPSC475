#Use of CMU pronouncing dictinoary

import nltk
#nltk.download('cmudict')
from nltk.corpus import cmudict
cmu = cmudict.dict()

def is_in_cmudict(word):
  if word in cmu:
    return True 
  return False 

def main():
  text = "these a from um youknow aargh bird's bird apple"
  text = text.split()

  wordLst = [word for word in text if is_in_cmudict(word)]
  print(wordLst)
main()
