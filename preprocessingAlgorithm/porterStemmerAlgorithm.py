import nltk
from nltk.stem import PorterStemmer

porter_stemmer = PorterStemmer()

def to_stem (text) :
    words = text.split()
    stemmed_text = [porter_stemmer.stem(word) for word in words]
    return stemmed_text

