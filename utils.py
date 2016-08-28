'''
  arg1 is the pattern to be matched
  arg2 is either the name of the file containing the string that is to be
    searched or the string itself
  arg3 is 'f' if arg2 is a file name
  arg4 is the number of matches to find. '0' finds all matches
  Usage:
    $pyton2.7
    >>>from utils import re_show
    >>>re_show('pat1','str1', 'f', 0)
    writes a file, re_show.txt, containing the string stored str1 
    with all occurences of the regex pat1 marked.

    >>>re_show.py('a',"Mary Ann stopped by Mona's",'s' 1)
    displays the input string with the first instance of 'a' marked
'''

def re_show(pat_in, strg_in, mode,times):
    import re
    if mode == 'f':
        strg = open(strg_in).read()
        pat = open(pat_in).readline().strip()
    else:
        strg = strg_in
        pat = pat_in
    pat_obj = re.compile(pat)

    #this curious syntax surrounds the pattern found by braces
    if (times > 0):
        str_out = pat_obj.sub("{\g<0>}",strg,times)
    else:
         str_out = pat_obj.sub("{\g<0>}",strg)

    if mode == 'f':
        fout = open("re_show.txt","w")
        fout.write(str_out)
    else:
        print str_out

'''
  arg1 is the name of the corpus
  arg2 is the name of the identifier within the corpus
  Usage:
    $pyton2.7
    >>>from utils import read_corpus
    >>>read_corpus('brown','editorial')
    writes a file, arg2.txt
'''
def read_corpus(corpus,id):
    import nltk
    if corpus == 'brown':
        from nltk.corpus import brown
        sentences = brown.sents(categories=id)
    if corpus == 'gutenberg':
        from nltk.corpus import gutenberg
        sentences = gutenberg.sents(id)
    sent_lst = [' '.join(sent) + '\n' for sent in sentences]
    txt = ''.join(sent_lst)
    id = id.split('.')  #eliminate the final 'txt' from gutenberg files
    filename = id[0] + '.txt' 
    outfile = open(filename, 'w') 
    outfile.write(txt)
    outfile.close()

                       
    

