import string


def to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def tokenization(text):
    text = to_lowercase(text)
    text = remove_punctuation(text)
    tokenized_text = text.split()
    return tokenized_text