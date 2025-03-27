#Surface forms or lemmas.  idea from ChatGPT

import spacy
from collections import Counter

def main():
  inp = "These are the uh dunno uhm days his for a I bird's birds isn't"
  illegal = {'uh', 'uhm'} #strings to pass over
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(inp) 
  print(inp)
  surface_counts = Counter(token.text.lower() for token in doc if token.is_alpha and token.text not in illegal)
  lemma_counts = Counter(token.lemma_.lower() for token in doc if token.is_alpha and token.text not in illegal)

  print("Surface Counts")
  for word,count in surface_counts.most_common():
    print(f"{word}: {count}")

  print()

  print("Lemma Counts")
  for word,count in lemma_counts.most_common():
    print(f"{word}: {count}")
main()

   
