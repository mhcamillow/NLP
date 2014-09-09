# -*- coding: utf-8 -*-

from unicodedata import normalize
import re, collections

#Primeira tentativa de trabalhar com n-gramas
class NLP():

  def __init__(self):
    self.texto = self.removeacentos(file('/home/camillo/src/trainingset.txt').read())
    self.lista = re.findall(r'[a-zA-Z]+', self.texto)

  def bigram(self, lista, w):
    r = []
    for idx, word in enumerate(lista):
      if (lista[idx-1] == w):
        r.append(word)
    return r
  #Melhorar isso aqui. Dá pra fazer um metodo só que aceite n-gramas
  def trigram(self, lista, w1, w2):
    r = []
    for idx, word in enumerate(lista):
      if (lista[idx-2] == w1) and (lista[idx-1] == w2):
        r.append(word)
    return r

  def train(self, lista):
    r = collections.defaultdict(lambda: 0)
    for word in lista:
      r[word] += 1
    return r

  def removeacentos(self, texto):
    codif = 'utf-8'
    return normalize('NFKD', texto.decode(codif)).encode('ASCII', 'ignore')	

  def Consulta(self, w1, w2):
    return self.train(self.trigram(self.lista, w1, w2))

  def Consulta2(self, w1):
    return self.train(self.bigram(self.lista, w1))
