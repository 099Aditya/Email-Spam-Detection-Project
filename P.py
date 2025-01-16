import pandas as pd
messages=pd.read_csv('SMSSpamCollection',
sep='\t',names=["label","message"])
messages

## Data Cleaning And Preprocessing
import re
import nltk
nltk.download('stopwords') 

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

corpus=[]
for i in range(0,len(messages)):
    review=re.sub('[^a-zA-z]',' ',messages['message'][i])
    review=review.lower()
    review=review.split() #spilit text into words
    ##Stems each word to its root form.
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')] 
    review=' '.join(review)
    corpus.append(review)  #collects cleaned and preprocessed messages.
corpus

## Output Features
y=pd.get_dummies(messages['label'])  #convert spam,ham in numerical value
y=y.iloc[:,0].values

## Train Test Split(80%) 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(corpus,y,test_size=0.20)

## Create the Bag OF Words model
from sklearn.feature_extraction.text import CountVectorizer #CountVectorizer converts text into a matrix of token counts
## for Binary BOW enable binary=True
cv=CountVectorizer(max_features=2500,ngram_range=(1,2))

len(X_test),len(y_test)

## independent features
X_train=cv.fit_transform(X_train).toarray()
X_test=cv.transform(X_test).toarray()

#train naive model for classification
from sklearn.naive_bayes import MultinomialNB
spam_detect_model=MultinomialNB().fit(X_train,y_train)
spam_detect_model 

y_pred=spam_detect_model.predict(X_test)

from sklearn.metrics import accuracy_score,classification_report
accuracy_score(y_test,y_pred)
from sklearn.metrics import classification_report    #provides precision, recall, and F1-score
print(classification_report(y_test,y_pred))

## Train Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(corpus,y,test_size=0.20)

from sklearn.feature_extraction.text import TfidfVectorizer
tv=TfidfVectorizer(max_features=2500,ngram_range=(1,2))
X_train=tv.fit_transform(X_train).toarray()
X_test=tv.transform(X_test).toarray() #TfidfVectorizer converts text into a matrix 

from sklearn.naive_bayes import MultinomialNB
spam_tfidf_model = MultinomialNB().fit(X_train, y_train)

#prediction
y_pred=spam_tfidf_model.predict(X_test)

score=accuracy_score(y_test,y_pred)
print(score)

from sklearn.metrics import classification_report
print(classification_report(y_pred,y_test))