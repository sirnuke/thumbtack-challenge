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
      if w[0] == word:
        return
    self._words.append((word, sorted(word)))

  def find_matches(self, length=ANAGRAM_LENGTH, set_length=SET_LENGTH):
    matches = []
    data = {}
    if set_length:
      match_length = set_length
    else:
      match_length = 2
    for pair in itertools.combinations(self._words, length):
      n = pair[0][0] + ', ' + pair[1][0]
      t = ''.join(sorted(pair[0][1] + pair[1][1]))
      k = t[:KEY_LENGTH]
      if not k in data:
        data[k] = {}
      if t in data[k]:
        data[k][t].append(n)
        l = len(data[k][t])
        if set_length:
          if l > match_length:
            match_length += 1
            matches = [t]
          elif l == match_length:
            matches.append(t)
        else:
          if l == match_length + 1:
            matches.remove(t)
          elif l == match_length:
            matches.append(t)
      else:
        data[k][t] = [n]
    if not set_length:
      print "[length is {}]".format(match_length)
    for t in matches:
      k = t[:KEY_LENGTH]
      print '; '.join(data[k][t])

if __name__ == '__main__':
  set_length = SET_LENGTH
  if len(sys.argv) >= 2:
    if sys.argv[1][0] == '-':
      print "Usage: {} [set-length (default:max)]".format(sys.argv[0])
      exit()
    set_length = int(sys.argv[1])
    if set_length < 1:
      print "{}: Invalid set-length {}".format(sys.argv[0], sys.argv[1])
      exit()
  corpus = Corpus()
  corpus.stdin()
  corpus.find_matches(set_length=set_length)

