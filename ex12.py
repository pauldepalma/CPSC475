from nltk.corpus import inaugural


def my_open(file_name):
    fout = open(file_name, 'w')
    return fout

def main():
    file_ids = inaugural.fileids()
    washington = file_ids[0]
    fout = my_open(washington)
    txt = ''
    for sent in inaugural.sents(washington):
        txt = ' '.join(sent) + '\n'
    ct = 0
    
    for i in range(len(txt)):
        print txt[i]
        if i % 10 == 0:
            print '\n'
        
        
        
        
    
    
main()
    
