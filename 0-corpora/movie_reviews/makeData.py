'''
Program to provide data for a movie review sentiment classifier training and testing

These NLTK corpora have to have been previously downloaded: movie_reviews, stopwords
to do so:
bring up python3
then:
>>>import nltk
>>>nltk.download('movie_reviews')
>>>nltk.download('stopwords')
'''
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import random

def makeReviewLsts(category,fract):
    trainLst = movie_reviews.fileids(category) #this is winnowed below
    tstNum = int(fract * len(trainLst))  #number of test reviews to set aside

    #randomly choose reviews for testing and remove them from training
    tstLst = []
    for i in range(tstNum):
        idx = random.randint(0,len(trainLst) - 1)
        tstLst.append(trainLst[idx])
        trainLst.pop(idx);
    return trainLst, tstLst

def makeBagOfWords(reviewLst):
    '''
    Extract words for each review
    Throw out those that are not alphabetic as well as short frequent English words
    Add the result to bag
    At the end, bag will be the list of words in a certain category of review.
    Use NLTK functions
    '''
                  
    bag = []
    for review in reviewLst:
        words = movie_reviews.words(review)  #list of words in a review 
        words = [word for word in words if word.isalpha()] #remove items witn non-alpha chars
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words] #stop words removed
        bag = bag + words
    return bag


def writeFile(fileName,dataName):
    with open(fileName,'w') as fout:
        for item in dataName:
            fout.write('%s\n' %item)
    fout.close()

    
def main():
    '''
    pos & neg hold files names containing positive and negative reviews minus
    those set aside for testing.
    posTst and negTst hold file names of positve and negatives set aside for
    testing.
    '''

    testFract = 0.10 #fraction of training data devoted to testinbg
    pos, posTst = makeReviewLsts('pos',testFract)
    
    neg, negTst = makeReviewLsts('neg',testFract)

    posBagOfWords = makeBagOfWords(pos)
    negBagOfWords = makeBagOfWords(neg)

    writeFile('pos.txt',posBagOfWords)
    writeFile('neg.txt',negBagOfWords)
    
    writeFile('posTst.txt',posTst)
    writeFile('negTst.txt',negTst)
        
    
main()
