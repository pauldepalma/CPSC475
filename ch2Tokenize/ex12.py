'''
Demonstrates:
    Extracting text from NLTK corpora
    
    To load corpora:
    Bring up a python shell
    >>import nltk
    >>nltk.download()
    Choose the identifier,'book'

    'book' refers to item 24 in Readings/Videos.

    The three corpora we will use are:
    *   gutenberg, a selection from the Gutenberg Corpus (www.gutenberg.org) a collection
        of 57,000 electronic texts
    *   inaugural, the U.S. presidential inaugural addresses
    *   brown, the first 1,000,000 word electronic corpus 
        (see http://icame.uib.no/brown/bcm-los.html for the contents)

    To find what's available in gutenberg:
    >>import nltk
    >>nltk.corpus.gutenberg.fileids()

    To find what's available in inaugural:
    >>nltk.corpus.inaugural.fileids()

    To find what's available in brown:
    >>import nltk
    >>nltk.corpus.brown.categories()

    The NLTK project provides lots software to read and analyze its corpora.  In most cases, I'd like you to write
    your own.  This function will transform an NLTK corpus to a conventional file

    Usage:
        bring up a python shell
        >>>from ex12 import write_corpus
        >>>write_corpus('brown','editorial')
        writes a file, editorial.txt
 '''

def write_corpus(corpus,id):
    import nltk
    if corpus == 'brown':
        from nltk.corpus import brown
        sentences = brown.sents(categories=id)
    if corpus == 'gutenberg':
        from nltk.corpus import gutenberg
        sentences = gutenberg.sents(id)
    if corpus == 'inaugural':
        from nltk.corpus import inaugural
        sentences = inaugural.sents(id)

    #sentences is a list of sentences from each inaugural address where
    #each sentence is a list of words

    #transform the corpus to a list of words
    sentLstU = [' '.join(sent) + '\n' for sent in sentences]

    #this line is new
    #transform the unicode encoded list of words to ascii
    sentLst = [item.encode('ascii','ignore') for item in sentLstU]

    #transform the list of words to a string
    txt = ''.join(sentLst)
    
    
    
    id = id.split('.')  #eliminate the final 'txt' from some corpora
    filename = str(id[0]) + '.' + str(id[1])
    outfile = open(filename, 'w') 
    outfile.write(txt) 
    outfile.close()



