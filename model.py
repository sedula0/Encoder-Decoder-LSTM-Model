'''
LSTM Encoder-Decoder Model that trains on language pairs, using keras
deep-learning.
'''


import csv
from pickle import dump, load

from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM, Dense, Embedding, RepeatVector, TimeDistributed
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils.vis_utils import plot_model
from numpy import array
from numpy.random import rand, shuffle

# Relative paths
pickled_data_path = 'data/'

# load a clean dataset
def load_clean_sentences(filename):
    return load(open(filename, 'rb'))

# save a list of clean sentences to file
def save_clean_data(sentences, filename):
    dump(sentences, open(filename, 'wb'))
    print('Saved: %s' % filename)


# Load dataset
raw_dataset = load_clean_sentences(pickled_data_path + 'ita.pkl')

# Reduce dataset size and set train/test split size
n_sentences = 10000
training_split = int(n_sentences * 0.9)
dataset = raw_dataset[:n_sentences, :]
# Random shuffle
shuffle(dataset)
# Split into train/test
train, test = dataset[:training_split], dataset[training_split:]
# Save
save_clean_data(dataset, pickled_data_path + 'ita-shuffled.pkl')
save_clean_data(train, pickled_data_path + 'ita-train.pkl')
save_clean_data(test, pickled_data_path + 'ita-test.pkl')

# Initialize seq2seq model
