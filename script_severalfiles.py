#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:00:49 2021

@author: agathamurgoci

THIS EXAMPLE RUNS THE COUNT WORDS FUNCTION FOR ALL THE FILES IN THE FOLDER TEXTS

"""

import re
from src import count_words
import os
folder_in = "texts/"
list_files = os.listdir(folder_in)
expr = r'\w+'
folder_out = "results/"
for i in range(len(list_files)):
    name_file = folder_in+list_files[i]
    text_file = open(name_file, 'r')
    text_data = text_file.read()
    text_file.close()
    list_wrds = re.findall(expr, text_data)
    result = count_words(list_wrds)
    name_res =folder_out+list_files[i]
    res_file = open(name_res, 'w')
    res_file.write(str(result))
    res_file.close()
    
## check the result of the     