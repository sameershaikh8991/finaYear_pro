import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

def tokenize(sentance):
	return nltk.word_tokenize(sentance)

def stem(word):
	return Stemmer.stem(word.lower())


def bag_of_words(tokenize_sentance,words):
	sentance_word = [stem(word) for word in tokenize_sentance]
	bag = np.zeros(len(words),dtype = np.float32)


	for idx , w in enumerate(words):
		if w in sentance_word:
			bag[idx] = 1

	return bag

