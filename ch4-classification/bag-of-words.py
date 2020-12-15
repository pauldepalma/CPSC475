
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

def main():
    
    reviews = movie_reviews.words() #all words from all reviews
    print("number of words in reviews: " + str(len(reviews)))
    print(movie_reviews.categories()) #positive and negative
    pos = movie_reviews.fileids() #all reviews
    posLst = movie_reviews.fileids('pos') #all  positive reviews
    review = movie_reviews.words('pos/cv000_29590.txt')  #list of words in a review
    review = ' '.join(review)  #make into string to tokenize
    tok = word_tokenize(review) #tokenize returns a list

    
    stop_words = set(stopwords.words('english')) #common small words
    filtered = [w for w in tok if w not in stop_words] #stop words removed

    #night make the classifier run faster. 
    f = nltk.FreqDist(filtered) #words and their frequencies 
    feature_vector = list(f)[:100] #most common 100 words
   
   
    
    
    
    

    
    
   
    
    
            
    
main()
