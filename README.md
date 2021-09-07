# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Solution
The solution uses the afinn library to perform sentiment analysis on the input.txt file. The language used was python. The afinn library assigns a score to every word between -5 and +5 and finds the sum.
I expected the overall score to be slightly positve because the first paragraph seemed to have a negative score and the second had a more positive score. The results were a 
positive score of 28 with stopwords and 24 without stopwords. Stopwords are words that are very commonly used such as "in," which can impact the score. Both results showed that the text was more positve than I expected

## Reflection
Going into this project I was very unfamiliar with python and never heard of sentiment analysis before. I was excited to learn new things but also nervous of failing the challenge. The solution is pretty straightforward, but I feel like a more complex solution could have been made, but wasn't necessary. 
While working on this project I got a lot more familiar with working in python. Overall I'm happy with what this challenge taught me.
##Libraries used
Afinn
Nltk

## Refrences 
I used this [website](https://www.kdnuggets.com/2018/08/emotion-sentiment-analysis-practitioners-guide-nlp-5.html) to teach me about sentiment analysis and afinn.
