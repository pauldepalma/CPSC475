#Use of both spacy and CMU
#I hope you see the problem with thinking of what we're counting as appearing in a dictionary
#at the command line:
#pip install spacy
#pip install nltk 
#python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm") #load English language model
import nltk
from nltk.corpus import cmudict

def main():
  cmu = cmudict.dict()
  words = set(cmu.keys())
  print("These" in words)
  disfluent = {'uh', 'uhm'} #strings to pass over
  inp = "These are the uh dunno uhm days his for a I bird's birds isn't"
  print(inp)
  doc = nlp(inp) #doc is a spacy object 
  #token is a spacy object
  tokens = [
            token.lower_ for token in doc
            if not token.is_space and not token.is_punct
           ]
  print(tokens)
 
  #capture only words
  tokens = [ 
            word for word in tokens 
            if word not in disfluent and word in words
           ]
  print(tokens) 


main()

