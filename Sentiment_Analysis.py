#Sentiment Analysis
#This program uses a lexicon to perform sentiment analysis
#this solution uses afinn lexicon for sentiment analysis
#a score is calculated with and without stop words
from afinn import Afinn
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

#function for printing the results
def printScore(score):
    if score> 0:
        print("The text has a positive sentiment of", end = " ")
    elif score < 0:
        print("The text has a negative sentiment of", end = " ")
    else:
        print("the text has a neutral sentiment of", end = " ")
    print(score)
  
#create variables
score_with_sw = 0.0
score2 = 0.0
tempscore = 0.0
score_no_sw = 0.0
afn = Afinn()

#open the input file
input_file = open("input.txt")
unedited_text = (input_file.read())
stop_words = stopwords.words('english')

#remove the puctuation and make it all lower case
edited_text = unedited_text.translate(str.maketrans('', '', string.punctuation))
edited_text = edited_text.lower()

#remove stopwords
edited_text_tokens = word_tokenize(edited_text)
text_no_stop_words = [word for word in edited_text_tokens if not word in stop_words]



#calculate the score based on the lexicon
score_with_sw = afn.score(edited_text)

size = len(text_no_stop_words)
i = 0

while i < size: 
    tempscore = afn.score(text_no_stop_words[i])
    score_no_sw += tempscore
    i += 1

#print the results
print("no stop words:")
printScore(score_no_sw)
print("with stop words:")
printScore(score_with_sw)