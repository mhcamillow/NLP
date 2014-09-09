# -*- coding: utf-8 -*-

from unicodedata import normalize
import re, collections

class NLP():

  def __init__(self):
    self.texto = self.normalize_text(file('big.txt').read())
    self.lista = re.findall(r'[a-zA-Z]+', self.texto)

  def ngram(self, previous_words):
    possible_words = collections.defaultdict(lambda: 0)

    for i, known_word in enumerate(self.lista):
      for x, previous_word in enumerate(previous_words):
        if (previous_word.lower() != self.lista[i + x]):
          break;
      else:
        possible_words[self.lista[i + len(previous_words)]] += 1

    return possible_words

  def train(self, lista):
    r = collections.defaultdict(lambda: 0)
    for word in lista:
      r[word] += 1
    return r

  def normalize_text(self, texto):
    codif = 'utf-8'
    return normalize('NFKD', texto.decode(codif)).encode('ASCII', 'ignore').lower()

#Example:
a = NLP()
print(dict(a.ngram(['you'])))
