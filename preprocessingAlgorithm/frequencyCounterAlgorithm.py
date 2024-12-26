import string
from preprocessingAlgorithm.tokenizeAlgorithm import tokenization


def frequencyCounter(text) :

    tokenized_text = tokenization(text)
    word_frequency = {}
    for word in tokenized_text :
        if word in word_frequency :
            word_frequency[word] += 1
        else :
            word_frequency[word] = 1

    return word_frequency           
