import matplotlib.pyplot as plt

'''
Demonstrates:
    A plot of Zipf's Law using P. Obama's inaugural address. 
    Usage (from the command line): python3 ex17.py
'''


'''
pre: string_in is a string
post: returns two lists: rank contains integers from 1 to n, where n is the number of
      words in the strong; freq contains the frequency of each word
      If you lined the lists up with rank on the left and frequency on the right,
      the first item in rank corresponds to the most frequent word in the input string.
      The first item in freq is the number of times that word appears in the string.
'''
def createPlotData(string_in):
    '''
    using a dictionary to count the words in the string.  The result is a 
    dictionary where each entry has this form {word:num}.  "word" is a word in the
    string.  "num" is the number of times it appears
    '''
    
    word_lst = string_in.split()
    count_dict = {}
    for word in word_lst:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1

    #values() extracts the num component from each {word:num} entry
    word_lst = list(count_dict.values())
    #put nums in reverse order, where the num of the most frequent word
    #is on top of the list
    word_lst.sort(reverse=True)

    #i+1 and i-1 is to compensate for lists starting a 0
    rank = [i+1 for i in range(len(word_lst))]
    freq = [word_lst[i-1] for i in rank]
    
    return rank, freq

def doPlot(rank,freq):
   plt.plot(rank,freq) 
   plt.show()

def main():
    fin = open("obama.txt", 'r')
    text = fin.read()
    fin.close
    
    rank, freq = createPlotData(text)
    doPlot(rank,freq)
   
    
main()
    
