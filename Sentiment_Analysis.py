#Sentiment Analysis
#This program uses a lexicon to perform sentiment analysis
#this solution uses afinn lexicon for sentiment analysis
from afinn import Afinn
from nltk import word_tokenize
import nltk
import string

  
#create variables
total_score = 0.0
score2 = 0.0
afn = Afinn()

#open the input file

input_file = open("input.txt")
unedited_text = (input_file.read())

#remove the puctuation and make it all lower case
edited_text = unedited_text.translate(str.maketrans('', '', string.punctuation))
edited_text = edited_text.lower()

#print(edited_text)
#calculate the score based on the lexicon
total_score = afn.score(edited_text)

#print the results
if total_score > 0:
    print ("The text has a positive sentiment of ", end = " ")
elif total_score < 0:
    print ("The text has a negative sentiment of ", end = " ")
else:
    print ("the text has a neutral sentiment of ", end = " ")
print (total_score)
