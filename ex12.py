'''
Demonstrates:
    How to transform an inaugural address from the NLTK corpus to a file

    To load corpora:
    >>import nltk
    >>nltk.download
    Choose the identifier,'book'
'''
from nltk.corpus import inaugural

def write_file(address):
    fout = open(address, 'w')
    for sent in inaugural.sents(address):
        sent = ' '.join(sent)
        fout.write(sent + '\n')  

def main():
    #the file_ids is a list of the names of all inaugural addresses
    #E.g., George Washington's is: 1789-Washington.txt
    file_ids = inaugural.fileids()
    address = file_ids[0]
    write_file(address)
    
main()
    
