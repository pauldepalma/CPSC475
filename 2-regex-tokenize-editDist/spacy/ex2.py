#Use of spacy to tokenize
#at the command line:
#pip install spacy
#python -m spacy download en_core_web_sm

import spacy

def main():
  nlp = spacy.load("en_core_web_sm") #load English language model
  disfluent = {'uh', 'uhm'} #strings to pass over

  text = "These are the uh dunno uhm days his for a I bird's birds isn't"
  doc = nlp(text)

  #a token is a spacy object. text extracts to text portion
  tokens = [token.text for token in doc if token.text not in disfluent]
  print(tokens) 


main()
