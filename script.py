#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:30:56 2021

@author: agathamurgoci

This example takes in a string containing the filename and prints the result of the word count

youcan use, for example texts/text.txt
"""

import re
from src import count_words, take_file


# if we want to test more examples, such files are in the folder texts
# to load a ist of all the files in the folder

name_file = input("Give ne a filename:")

text_data = take_file(name_file)


expr = r'\w+'

list_wrds = re.findall(expr, text_data)
result = count_words(list_wrds)
    

print(result)