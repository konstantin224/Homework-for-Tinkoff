

import re

import random

import numpy as np



import codecs

word = []

with codecs.open("text.txt","r","utf-8") as text: #проводим токенизацию
    for line in text:
        t = re.split('[^а-я]', line.lower().strip())
        while "" in t:
            t.remove("")
        for i in range(len(t)):
            word.append(t[i])





length = int(input())

ngrams = {}

for i in range(len(word)-n): #создаём n-граммы
    gram = " ".join(word[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(word[i+n])





sentence = " ".join(word[0:n]) # Делаем генерацию
anw = sentence

for i in range(200):
    if sentence not in ngrams.keys():
        break
    possible_words = ngrams[sentence]
    next_word = possible_words[random.randrange(len(possible_words))]
    anw += ' ' + next_word
    sentence_word = re.split('[^а-я]', anw.lower().strip())
    while "" in sentence_word:
        sentence_word.remove("")
    sentence = ' '.join(sentence_word[len(sentence_word)-n:len(sentence_word)])

        


print(anw)





