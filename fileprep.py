'''
This program takes in raw data (language pairs) and
converts itinto a usable dataset after cleaning.
Exports as csv files and/or pickled (serialized) files.
Finished pairs are in the form of [{English} {Other Language}],
with punctuation removed.

To do: identify optimal cleaning process, especially for languages without
latin script.
'''


import re
import string
from pickle import dump
from unicodedata import normalize

# import pandas as pd
from numpy import array


# Load file into memory.
def load_file(filename):
    file = open(filename, mode='rt', encoding='utf-8')
    text = file.read()
    file.close()
    return text

# # Save text onto new csv file.
# # me using pandas to do this :P
# def save_file(text_list, filename, path):
#     df = pd.DataFrame(text_list)
#     df.to_csv(path + f'{filename}.csv', index=False, header=False)

# Split language pairs based on tab delimiter and remove CC credits.
def split_pairs(text):
    lines = text.strip().split('\n')
    pairs = [line.split('\t')[:2] for line in lines]
    return pairs

# Make the actual csv file(s).
def make_csv(langs=['cmn', 'fra', 'ita', 'rus', 'spa', 'vie', 'kor', 'jpn']):
    for lang in list(langs):
        save_file(split_pairs(
            load_file(data_path + f'{lang}.txt')), f'{lang}', data_path)


# Store relative paths
data_path = 'data/'

# Data Cleaning WOOHOO

# Cleans up the following:
#   Removes non-printable characters
#   Removes punctuation
#   Converts to Unicode to ASCII
#   Makes lowercase
def clean_pairs(lines):
    cleaned = []
    # prepare regex for char filtering
    re_print = re.compile('[^%s]' % re.escape(string.printable))
    # prepare translation table for removing punctuation
    table = str.maketrans('', '', string.punctuation)
    for pair in lines:
        clean_pair = []
        for line in pair:
            # normalize unicode characters
            line = normalize('NFD', line).encode('ascii', 'ignore')
            line = line.decode('UTF-8')
            # tokenize on white space
            line = line.split()
            # convert to lowercase
            line = [word.lower() for word in line]
            # remove punctuation from each token
            line = [word.translate(table) for word in line]
            # remove non-printable chars form each token
            line = [re_print.sub('', w) for w in line]
            # remove tokens with numbers in them
            line = [word for word in line if word.isalpha()]
            # store as string
            clean_pair.append(' '.join(line))
        cleaned.append(clean_pair)
    return array(cleaned)

# Remove duplicate pairs
def clean_dupes(lines):
    no_dupes_set = set(tuple(pair) for pair in lines)
    no_dupes_list = [list(pair) for pair in no_dupes_set]
    return array(no_dupes_list)

# mmm pickles
def pickle_data(data, filename):
    dump(data, open(filename, 'wb'))
    print(f'Pickled: {filename}')

# Put it all together
def make_pairs(lang):
    return clean_dupes(clean_pairs(split_pairs(load_file(data_path + f'{lang}.txt'))))


data = make_pairs('ita')
pickle_data(data, 'ita.pkl')
