import streamlit as st
import joblib
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def load_tfidf():
    tfidf = joblib.load(open("feature.pkt.pkt", "rb"))
    return tfidf

def load_model():
    nb_model = joblib.load(open("toxic model.pkt.ptk", "rb"))
    return nb_model

def toxic_prediction(text):
    tfidf = load_tfidf()
    text_tfidf = tfidf.transform([text]).toarray()
    nb_model = load_model()
    prediction = nb_model.predict(text_tfidf)
    class_name = "Toxic" if prediction == 1 else "Non-Toxic"
    return class_name

st.header("Toxic Comment Detection Web App")

# Add your image above the result section
image_path = "toxic.jpg" 
st.image(image_path, caption="Toxic Comment Detection", use_column_width=True)

st.subheader("Input your text")
text_input = st.text_input("Enter your comment:")

if text_input is not None:
    if st.button("Detect"):
        result = toxic_prediction(text_input)
        st.subheader("Result:")
        st.info("The result is " + result + ".")
