import string
import nltk


from nltk import word_tokenize,sent_tokenize
from nltk.stem.porter import PorterStemmer

# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def string_prepare(sentence: str):
    stemmer = PorterStemmer()
    sentence = sentence.lower()
    sentence = "".join([ch for ch in sentence if ch not in string.punctuation])
    tokens = nltk.word_tokenize(sentence)
    stems = stem_tokens(tokens, stemmer)
    str_to_return = ""
    for stem in stems:
        str_to_return += stem + " "
    return str_to_return


def del_stop_words(sentence):
    stop = set(stopwords.words('english'))
    sentence_to_return = ""
    for i in sentence.lower().split():
        if i not in stop:
            sentence_to_return += i + " "
    return sentence_to_return


def message_process(messages):
    correct_messages = []
    for message in messages:
        message = del_stop_words(message)
        message = string_prepare(message)
        correct_messages.insert(len(correct_messages), message)
    return correct_messages


