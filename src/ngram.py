# -*- coding: utf-8 -*-

from unicodedata import normalize
import re, collections

class NLP():

  def __init__(self):
    self.text = self.normalize_text(open('big.txt', encoding='ASCII').read())
    self.known_words = re.findall(r'[a-zA-Z]+', self.text)

  def ngram(self, previous_words):
    possible_words = collections.defaultdict(lambda: 0)

    for i, known_word in enumerate(self.known_words):
      for x, previous_word in enumerate(previous_words):
        if (previous_word.lower() != self.known_words[i + x]):
          break;
      else:
        possible_words[self.known_words[i + len(previous_words)]] += 1

    return possible_words

  def normalize_text(self, text):
    codif = 'utf-8'
    return normalize('NFKD', text).lower()

#Example:
a = NLP()
print(dict(a.ngram(['the', 'king'])))
