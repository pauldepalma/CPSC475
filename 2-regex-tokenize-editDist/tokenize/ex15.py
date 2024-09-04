'''
Illustrates two tokenizers, one home-grown (simpleT), the other from NLTK (NLTK)
Execution from the command line: python3 ex16.py corpus tokenizer
'''

from nltk.tokenize import word_tokenize
from collections import Counter
import string
import sys

def getData(fname):
    fin = open(fname, 'r')
    
    text = fin.read()  #read in text as a string
    fin.close()
    return text

def tokenize(text):

    #discover non-ascii characters
    #Project Gutenberg uses lots of them
    dict = {ord(ch) : ch for ch in text if ord(ch) > 127}
    nonAscii = ''.join(list(dict.values()))

    #splitting on white space works fine
    word_lst = text.split()

    #characters to be removed from the text
    remove = string.digits + string.punctuation + nonAscii
    
    #map characters to be removed(key) to 'None'(value)
    #empty params indicate key/value pairs are implicit in remove
    table = str.maketrans('','',remove)
    
    #for each word in word_list, substitute the mapping, i.e., 'None'
    word_lst = [w.translate(table) for w in word_lst]

    #Remove empty words from the list. length of None is 0
    word_lst = [word for word in word_lst if len(word) > 0]
   
    word_lst = [word.lower() for word in word_lst]

    #Remove invalid single letter words from list:
    word_lst = [word for word in word_lst if len(word) > 1 or
                word == 'i' or word == 'a']

    return word_lst


def count_words(word_lst):

    #it's more fun to do this with a dictionary

    word_dict = Counter(word_lst)
    
    return word_dict
    
def display(word_dict):
    for word in word_dict.keys():
        print(word + '\t\t' + str(word_dict[word]))

def stats(word_lst, word_dict, tokenizer):
    print("Tokenizer: " + tokenizer)
    V = len(word_dict.keys())
    N = len(word_lst)
    print("Tokens: " + str(N))
    print("Types: " + str(V))
    print ("Ratio of Types to Tokens: ", str(V/N))

    
def main():

    file_name = sys.argv[1]
    tokenizer = sys.argv[2]
    
    text = getData(file_name)

    if tokenizer == "simpleT":
        word_lst = tokenize(text)
   
    if tokenizer == "NLTK":
        word_lst = word_tokenize(text)
        
    print(word_lst)
    #count words
    #word_dict = count_words(word_lst)

    #stats(word_lst, word_dict,tokenizer)
    
    #display words
    #display(word_dict)
            
    
main()
