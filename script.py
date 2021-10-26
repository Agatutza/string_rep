#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:30:56 2021

@author: agathamurgoci
"""

import re
from src import count_words


# if we want to test more examples, such files are in the folder texts
# to load a ist of all the files in the folder

name_file= "texts/text.txt"
text_file = open(name_file, 'r')
text_data = text_file.read()
text_file.close()

expr = r'\w+'

list_wrds = re.findall(expr, text_data)
result = count_words(list_wrds)
    

print(result)