'''
Demonstrates:
    Extracting text from NLTK corpora

    see also: www.nltk.org/book/ch02.html ("Accessing Text Corpora and Lexical Resources")
    
    To load corpora:
    Bring up a python shell
    >>import nltk
    >>nltk.download()
    Choose the identifier,'book'

    'book' refers to item 24 in Readings/Videos.

    The three corpora we will use are:
    *   gutenberg, a selection from the Gutenberg Corpus (www.gutenberg.org) a collection
        of 57,000 electronic texts (http://www.gutenberg.org)
    *   brown, the first 1,000,000 word electronic corpus 
        (see http://icame.uib.no/brown/bcm-los.html for the contents)
    *   presidential innaugural addresses

    To find what's available in gutenberg:
    >>import nltk
    >>nltk.corpus.gutenberg.fileids()

    To find what's available in inaugural:
    >>nltk.corpus.inaugural.fileids()

    To find what's available in brown:
    >>import nltk
    >>nltk.corpus.brown.categories()

    The NLTK project provides lots software to read and analyze its corpora.  
    In most cases, I'd like you to write
    your own.  This function will transform an NLTK corpus to a conventional file

    Usage:
        bring up a python shell
        >>>from ex13 import write_corpus
        >>>write_corpus('brown','editorial')
        writes a file, editorial.txt
 '''

def write_corpus(which,id):
    import nltk
    if which == 'brown':
        from nltk.corpus import brown
        sentences = brown.sents(categories = id)
    if which == 'gutenberg':
        from nltk.corpus import gutenberg
        sentences = gutenberg.sents(id)
    if which == 'inaugural':
        from nltk.corpus import inaugural
        sentences = inaugural.sents(id)

    #sentences is a list of sentences where each sentence is a list of words

    #transform the corpus to a list of words
    lst = [' '.join(sent) + '\n' for sent in sentences]
    text = ' '.join(lst)
    
    
    filename = which + '.' + id
    outfile = open(filename, 'w') 
    outfile.write(text) 
    outfile.close()



