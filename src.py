#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:15:07 2021

@author: agathamurgoci
"""
def count_words(list_words):
    n = len(list_words)
    dict_words = {}
    for i in range(n):
        word = list_words[i].lower()
        if word not in dict_words.keys():
            n_w = 1
            for j in range(i+1,n):
                if list_words[j].lower() == word:
                    n_w +=1
                else:
                    continue
            dict_words[word]=n_w   
        else:
            continue
    return dict_words

def take_file(filename):
    text_file = open(filename, 'r')
    text_data = text_file.read()
    text_file.close()
    return text_data

