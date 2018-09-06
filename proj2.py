'''
Demonstrates
    file operations: open, close, read entire file, read a line at a time
    testing for file existence
'''
import nltk
from nltk.corpus import inaugural



def main():
    ids = inaugural.fileids()
    id = ids[0]
    for w in inaugural.words(id):
        if w in ['free', 'freedom', 'citizen']:
            print id
            
    
    
    
    
    

main()

   


