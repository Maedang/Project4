import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import re
from nltk.tokenize import word_tokenize
import pandas as pd
import snscrape.modules.twitter as sntwitter
# Others
import nltk
from nltk.stem.snowball import SnowballStemmer
from keras import backend as K
import string
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')


def get_tweets(username):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{username}').get_items()):
        tweets.append(tweet.content)
        if i == 50: break
    return tweets

def load_files():
    try:
        with open("models/LSTM_E-I.sav", "rb") as file:
            ei_classifier = pickle.load(file)
        with  open("models/LSTM_N-S.sav", "rb") as file:
            ns_classifier = pickle.load(file)
        with open("models/LSTM_F-T.sav", "rb") as file:
            ft_classifier = pickle.load(file)
        with  open("models/LSTM_J-P.sav", "rb") as file:
            jp_classifier = pickle.load(file)
    except FileNotFoundError:
        print("Model not found!")

    return ei_classifier, ns_classifier, ft_classifier, jp_classifier; 
    
def  clean_text(text):
    stopword_list = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    
     ## Remove puncuation
    text = text.translate(string.punctuation)
    
    ## Convert words to lower case and split them
    text = text.lower().split()
    
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops and len(w) >= 3]
    
    text = " ".join(text)
    ## Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    ## Stemming
    text = text.split()
    stemmer = SnowballStemmer('english')
    stemmed_words = [stemmer.stem(word) for word in text]
    text = " ".join(stemmed_words)
    return text

def get_prediction(username):
    ei_classifier, ns_classifier, ft_classifier, jp_classifier, vectorizer = load_files()
    tweets = get_tweets(username)
    text   = " ".join(tweets)
    text = text.map(lambda x: clean_text(x))
    vocabulary_size = 20000
    tokenizer = Tokenizer(num_words= vocabulary_size)
    tokenizer.fit_on_texts(text)
    sequences = tokenizer.texts_to_sequences(training_data['cleaned_post'])
    data = pad_sequences(sequences, maxlen=50)
    
    prediction = ""
    e_or_i = "E" if ei_classifier.predict(data)[0] == 1 else "I"
    n_or_s = "N" if ns_classifier.predict(data)[0] == 1 else "S"
    f_or_t = "F" if ft_classifier.predict(data)[0] == 1 else "T"
    j_or_p = "J" if jp_classifier.predict(data)[0] == 1 else "P"
    prediction = e_or_i + n_or_s + f_or_t + j_or_p

    return prediction, tweets

