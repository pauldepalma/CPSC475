'''
Illustrates two tokenizers, one home-grown (simpleT), the other from NLTK (NLTK)
Writes results to a csv file
Execution from the command line: python3 ex15A.py input output
'''

from nltk.tokenize import word_tokenize
from nltk.corpus import cmudict
from collections import Counter
import string
import sys
import csv
import re 

def readData(fname):
    fin = open(fname, 'r')
    text = fin.read()  #read in text as a string
    fin.close()
    return text
    
def writeData(fname,word_dict):
	tuples_lst = list(word_dict.items())
	sorted_lst = sorted(tuples_lst, key=lambda x: x[1], reverse=True)
	
	with open(fname, 'w', newline = '') as csvfile:
	    writer = csv.writer(csvfile)
	    for tuple in sorted_lst:
	        writer.writerow([tuple[0],tuple[1]])
	
def tokenize(text):
	
    #discover non-ascii characters
    dict = {ord(ch) : ch for ch in text if ord(ch) > 127}
    nonAscii = ''.join(list(dict.values()))
    
    #Santa Barbara: remove names of interlocutors
    text = corpusSpecific(text)
    
    #split on spaces
    word_lst = text.split()

    #to count contractions like I'm
    punctuation = string.punctuation.replace("'","")
    #characters to be removed from the text
    remove = string.digits + punctuation + nonAscii

    #Creates a dictionary of key/value pairs, where each character in 
    #remove is mapped to none as in:
    {'9' : None}
    trDict = str.maketrans('','',remove)
    
    #for each character in each word in word_list, substitute 'None'
    #This removes the character
    word_lst = [w.translate(trDict) for w in word_lst]
   
    #Remove empty words from the list. length of None is 0
    #word_lst = [word for word in word_lst if len(word) > 0]
    #print(word_lst)
   
    word_lst = [word.lower() for word in word_lst]

    #Remove invalid single letter words from list:
    word_lst = [word for word in word_lst if len(word) > 1 or
        word == 'i' or word == 'a']
    	
    #remove strings not in carnegie-mellon pronouncing dictionary
    cmu = cmudict.dict()
    word_lst = [word for word in word_lst if cmuDict(word,cmu)]
    
    return word_lst
    
def corpusSpecific(text):
	#Santa Barbara: remove names of interlocutors
    text = re.sub(r'[ \t][A-Z]+:[ \t]', ' ', text)
    return text
	
def cmuDict(word,cmu):
    if word in cmu:
        return True
    return False


def count_words(word_lst):
    word_dict = Counter(word_lst)
    '''
    with a dictionary
    word_dict = {}
    for word in word_list:
    	if word_dict(word)
            word_dict[word] = word_dict[word] + 1
    	else
    	    word_dict[word] = 1
    '''
    return word_dict
    

    
def main():

    input = sys.argv[1]
    output = sys.argv[2]
    
    text = readData(input)
   
    word_lst = tokenize(text)
   
    #count words
    word_dict = count_words(word_lst)
    
    #write to csv file
    writeData(output,word_dict)
	    

    
  
    
main()
