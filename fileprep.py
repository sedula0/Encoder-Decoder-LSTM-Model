import os

import pandas as pd


# load language pairs into memory
def load_text(filename):
    file = open(filename, mode='rt', encoding='utf-8')
    text = file.read()
    file.close()
    return text

# save text onto new csv file
# me using pandas to do this :P
def save_file(text_list, filename, path):
    df = pd.DataFrame(text_list)
    df.to_csv(path + f'{filename}.csv', index=False, header=False)

# split language pairs based on tab and remove cc credits
def split_pairs(text):
    lines = text.strip().split('\n')
    pairs = [line.split('\t')[:2] for line in lines]
    return pairs


path = '/data/'
langs = ['cmn', 'fra', 'ita', 'rus', 'spa', 'vie', 'tel', 'kor', 'jpn']
for lang in langs:
    save_file(split_pairs(load_text(path + f'{lang}.txt')), f'{lang}', path)
