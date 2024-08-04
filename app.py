import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import  PorterStemmer
import string


ps=PorterStemmer()

def trans(Text):
    Text=Text.lower()
    Text= nltk.word_tokenize(Text)

    y = []
    for i in Text:
        if i.isalnum():
           y.append(i)
    Text=y[:]
    y.clear()

    for i in Text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    Text=y[:]  
    y.clear()


    for i in Text:
        y.append(ps.stem(i))


    return " ".join(y)

cv = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email Spam Clasaifier")
st.write('This is a simple Email Spam Classifier using Machine Learning')

message = st.text_area("Enter the Email Text", height=300)
 
if st.button("Predict"):
    # Preprocess

    data = trans(message)
    # vectorize data
    vect = cv.transform([data])
     # make prediction
    result = model.predict(vect)
    if result == 1:
        st.error('This is a Spam Email')
    else:
        st.success('This is a Not Spam Email')