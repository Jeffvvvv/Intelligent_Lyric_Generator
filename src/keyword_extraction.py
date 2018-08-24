#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:34:30 2018

@author: chloezeng
"""

# Adapted from: github.com/aneesha/RAKE/rake.py
from __future__ import division
import unicodedata
import operator
import nltk
import string
from nltk.stem.porter import *


def isPunct(word):
      if len(word) == 1 and word in string.punctuation:
          return True
      else:
          return False

def isNumeric(word):
      if len(word) != 1:
          return False
      try:
          float(word) if '.' in word else int(word)
          return True
      except ValueError:
          return False
      
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

class RakeKeywordExtractor:

  def __init__(self):
    self.stopwords = set(nltk.corpus.stopwords.words())

  def _generate_candidate_keywords(self, sentence): # remove punct, stopwords and numbers & stemming
    words = map(lambda x: "|" if x in self.stopwords else x,
                nltk.word_tokenize(sentence.lower()))
    candi_keywords = []
    for word in words: 
        if word != "|" and not isPunct(word) and not isNumeric(word):
                candi_keywords.append(word)
    stemmer = PorterStemmer()
    candi_keywords = [stemmer.stem(word) for word in candi_keywords]

    return candi_keywords

  def _calculate_word_scores(self, phrase_list):
    word_freq = nltk.FreqDist()
    word_degree = nltk.FreqDist()
    for phrase in phrase_list:
      degree = len(filter(lambda x: not isNumeric(x), phrase)) - 1
      for word in phrase:
        word_freq[word] += 1
        word_degree[word] += degree # other words
    for word in word_freq.keys():
      word_degree[word] = word_degree[word] + word_freq[word] # itself
    # word score = deg(w) / freq(w)
    word_scores = {}
    for word in word_freq.keys():
      word_scores[word] = word_degree[word] / word_freq[word]
    return word_scores

  def _calculate_phrase_scores(self, phrase_list, word_scores):
    phrase_scores = {}
    for phrase in phrase_list:
      phrase_score = 0
      for word in phrase:
        phrase_score += word_scores[word]
      phrase_scores[phrase] = phrase_score
    return phrase_scores
    
  def sen_extract(self, sentence, incl_scores=False, word_num=1):
    candi_keywords = self._generate_candidate_keywords(sentence)
    word_scores = self._calculate_word_scores(candi_keywords)
    phrase_scores = self._calculate_phrase_scores(
      candi_keywords, word_scores)
    sorted_phrase_scores = sorted(phrase_scores.iteritems(),
      key=operator.itemgetter(1), reverse=True)
    n_phrases = len(sorted_phrase_scores)
    if incl_scores:
      return sorted_phrase_scores[0:word_num]
    else:
      return map(lambda x: x[0],
        sorted_phrase_scores[0:word_num])
    
  def song_extract(self, texts, incl_scores=False, word_num=1):
      sentences = texts.split("\r")
      keywords = []
      for sentence in sentences:
          keyword = self.sen_extract(sentence, incl_scores, word_num)
          keywords.append(keyword)
          
      return keywords

'''def test():
      texts = """
      A lot of cats are hatin', slandering makin' bad statements
Mad cause they sit on their ass just stagnating
Always vacillatin', now classmates I graduated with
Are wonderin' how the stupidest kid up in the class made it
Sick landscapin' and jammin' down in my mans basement
Getting restraints and complaints from mad neighbors
Now prejudice bigots say I sound just like them damn #%#
Them pair of lenses ain't repairin' their impaired vision
I'm on a mission escaping my own prison
Inflicting more pain then you're givin' see I'm my own victim
I can't believe I let you take up my time
Take up space in mind, give it here, I'm takin' what's mine
(Chrous)
The only ounce of power that I have
Is what I do with now
And how I let the hours pass
I dont' know how long I'm gonna last
So I can't let ya snatch the powder out my hourglass
Everyday that I'm awake I face the angel of death
He may be taken my breath, so they can lay me to rest
And by now my inner state's the only place that I rep
The way that I dress is just another way to express
We know that some day everybody we see will be dead and rotten
Long forgotten, we oughta keep this for a normal topic
Because we all get caught up in all the drama
But what's the gossip gonna mean, when me and you are goners
See I never did audition for a part in this play
I know that some day I'll accidentally fall in my grave
So I can really give a shit about what all of ya say
According to me is how I'm spending all of my days
(Chorus)
The world will keep turnin', the inferno will keep burnin'
But it's affirmative my life on Earth is impermanent
And since I'm visiting and my minutes here are limited
I ain't havin' or doin' shit if I ain't feelin' it
I'll lend a hand to a hurt pedestrian and I will help a friend
In any way that I can, but I can't let man get up in the way of my plans
Make me stray from my path, I can't be takin' that chance
(Chorus)"""
      rake = RakeKeywordExtractor()
      sentences = texts.split("\n")
      print len(sentences)
      # print sentences
      keywords = []
      for sentence in sentences:
          keywords.append(rake.sen_extract(sentence))
      print keywords
      print len(keywords)
      
    
if __name__ == "__main__":
  test()'''
