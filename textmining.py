# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:15:58 2021

@author: Moonseog
"""
from collections import Counter
f = open('yesterday.txt','r', encoding='utf-8')
y_lyrics = f.readlines()

f.close()

# change y_lyrics to list of word
word_list = []
for i in y_lyrics:
    word_list.extend(i.upper().strip('\n').split())
#print(word_list)

# use Counter of collections to count the word found in word_list
y_count = Counter(word_list)
#print(dict(sorted(y_count.items(), key=lambda e:e[1], reverse=True)))
#print("Number of Yesterday in this song : ", y_count['YESTERDAY'])


def sort_key(e):
    return e[1]
# use function sorted to dictionary Counter object
for k,v in sorted(y_count.items(),key=sort_key, reverse=True):
    print(f"{k:>10}: {v:4}")
    
