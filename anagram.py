#!/usr/bin/env python2.7

import itertools
import re
import sys

ANAGRAM_LENGTH = 2
SET_LENGTH = None
MINIMUM_WORD_LENGTH = 4
KEY_LENGTH = 1

class Corpus(object):
  def __init__(self):
    self._words = []

  def stdin(self):
    for word in re.sub('[\W\d]+', ' ', sys.stdin.read()).split():
      self.add_word(word)

  def add_word(self, word):
    if len(word) < MINIMUM_WORD_LENGTH:
      return
    word = word.lower()
    for w in self._words:
      if w == word: return
    self._words.append(word)

  def find_matches(self, anagram_length=ANAGRAM_LENGTH, set_length=SET_LENGTH):
    matches = {}
    data = {}
    match_length = 2
    for pair in itertools.combinations(self._words, anagram_length):
      name = ', '.join(pair)
      s = set(pair)
      t = ''.join(sorted(''.join(pair)))
      key = t[:KEY_LENGTH]
      if not key in data: data[key] = {}
      if not t in data[key]: data[key][t] = []
      unique = True
      for existing in data[key][t]:
        if len(existing[1] & s) != 0:
          unique = False
          break
      if unique:
        data[key][t].append((name, s))
        matches[t] = len(data[key][t])
        if matches[t] > match_length: match_length = matches[t]
    if not set_length:
      print "(length is {})".format(match_length)
    else:
      match_length = set_length
    for t in matches:
      if matches[t] != match_length: continue
      for n in data[t[:KEY_LENGTH]][t]:
        sys.stdout.write("{}; ".format(n[0]))
      print

if __name__ == '__main__':
  corpus = Corpus()
  corpus.stdin()
  corpus.find_matches()

