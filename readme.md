# Sentiment Analysis App

## Overview
- Preprocesses text data (cleaning, stopword removal, lemmatization)
- Trains a **Logistic Regression** on IMDB movie reviews
- Uses **TF-IDF** for feature extraction
- Developed **Streamlit** Interface for interactive prediction

## Model
- **Dataset** : IMDB Dataset of 50K Movie Review
- **Encoding** :  
    - Positive -> 1
    - Negative -> 0
- **Best Model** : Logistic Regression
- Saved using joblib (sentiment_model.joblib, vectorizer.joblib) 

## Run the App
```bash 
streamlit run app.py 
```

## Example Prediction

Review         | Predicted Statement
---------------|--------------------
The movie was fantastic|Positive
This was the worst movie ever|Negative
Some scenes were good but the ending disappointed me|Negative  

## Tech Stack
- **Programming Languages:** Python
- **Libraries:** Scikit-learn, NLTK, Pandas, Streamlit
- **Framework:** Pandas, Matplotlib
- **Modelling:** Logistic regression, TF-IDF Vectorization


## Structure
```
Sentiment-Analysis/
├── app.py
├── models/
│   ├── sentiment_model.joblib
│   └── vectorizer.joblib
├── src/
│   └── preprocessing.py
└── notebooks/
    └── sentiment_analysis.ipynb
```

