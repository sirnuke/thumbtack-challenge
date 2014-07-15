#!/usr/bin/env python2.7

import itertools
import re
import sys

ANAGRAM_LENGTH = 2
ONLY_LONGEST = True
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
      if w[0] == word:
        return
    self._words.append((word, sorted(word)))

  def find_matches(self, length=ANAGRAM_LENGTH, only_longest=ONLY_LONGEST):
    matches = []
    data = {}
    match_length = 2
    for pair in itertools.combinations(self._words, length):
      n = pair[0][0] + ', ' + pair[1][0]
      t = ''.join(sorted(pair[0][1] + pair[1][1]))
      k = t[:KEY_LENGTH]
      if not k in data:
        data[k] = {}
      if t in data[k]:
        data[k][t].append(n)
        if len(data[k][t]) > match_length:
          match_length += 1
          matches = [t]
        elif len(data[k][t]) == match_length:
          matches.append(t)
      else:
        data[k][t] = [n]

if __name__ == '__main__':
  corpus = Corpus()
  corpus.stdin()
  corpus.find_matches()

