# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec

# Reads ‘alice.txt’ file
sample = open("alice.txt")
s = sample.read()

# Replaces escape character with space
f = s.replace("\n", " ")

data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
	temp = []
	
	# tokenize the sentence into words
	for j in word_tokenize(i):
		temp.append(j.lower())

	data.append(temp)

# Create Skip Gram model
model = gensim.models.Word2Vec(data, min_count = 1, vector_size = 100, window = 5, sg = 1)

# Print results
print("cat " + "grin", 
	model.wv.similarity('cat', 'grin'))
	
print("queen " + "head", 
	model.wv.similarity('queen', 'head'))

print("alice " + "queen", 
	model.wv.similarity('alice', 'queen'))

print("queen " + "king", 
	model.wv.similarity('queen', 'king'))

print("alice " + "beginning", 
        model.wv.similarity("alice", "beginning"))

print("alice " + "considering", 
        model.wv.similarity("alice", "considering"))

print("rabbit " + "riper", 
        model.wv.similarity("sister", "riper"))
