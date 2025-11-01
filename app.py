import streamlit as st
from src.predict import predict_sentiment

st.title("Movie Review Sentiment Analyzer")
st.write("Enter and IMDB review below and analyze sentiment:")

review = st.text_area("Movie review")

if st.button("Predict Sentiment:"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        sentiment = predict_sentiment(review)
        st.success(f"Predicted Sentiment: {sentiment}")