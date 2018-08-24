#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:55:04 2018

@author: chloezeng
"""

import csv
import enchant

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from nltk.corpus import words as nltk_words

def is_english_word(word):
    # creation of this dictionary would be done outside of 
    #     the function because you only need to do it once.
    dictionary = dict.fromkeys(nltk_words.words(), None)
    try:
        x = dictionary[word]
        return True
    except KeyError:
        return False
    
dic = enchant.Dict("en_US")
    
ifile = open('pop3.csv','rU')
reader = csv.reader(ifile)

songs = []
for row in reader:
   songs.append(row)
         
titles = []
for song in songs:
    titles.append(song[1])

ofile = open('pop_eng.csv', 'wb')
writer = csv.writer(ofile)

i = 0
for title in titles:
    isEng = True
    try: # able to encode
        words = title.split('-')
        for word in words:
            if dic.check(word) is False:
                isEng = False
                break
            else:
                continue
        if isEng:
                tmp = songs[i]
                writer.writerow(tmp)
                i += 1
        else:
                i += 1
    except UnicodeDecodeError:
        print ("Invalid characters!")
        i += 1

ofile.close()





