#!/usr/bin/env python2.7

import itertools
import re
import sys

_ORD_A = ord('a')
DEFAULT_ANAGRAM_LENGTH = 2
MINIMUM_WORD_LENGTH = 4

class Pair(object):
  def __init__(self, words):
    self.words = words
    self.key = 0
    self.length = 0
    for word in words:
      pass
    #  self.length += len(word)
      #for char in word.lower():
        #self.key |= 2**(ord(char) - _ORD_A)

class Corpus(object):
  def __init__(self):
    self._words = []
    self._composition = {}
    self.matches = []

  def stdin(self):
    #for line in re.sub('[\W\d]+', ' ', sys.stdin.read()).split('\n'):
    for line in sys.stdin:
      line = re.sub('[\W\d]+', ' ', line)
      for w in line.split():
        self.add_word(w)

  def add_word(self, word):
    if len(word) < MINIMUM_WORD_LENGTH:
      return
    word = word.lower()
    for w in self._words:
      if w == word:
        return
    self._words.append(word)

  def find_matches(self, length):
    for pair in itertools.permutations(self._words, length):
      p = Pair(pair)


if __name__ == '__main__':
  anagram_length = DEFAULT_ANAGRAM_LENGTH
  if len(sys.argv) > 2:
    if sys.argv[1][0] == '-':
      print "Usage: {} [anagram-length]".format(sys.argv[0])
      print
      print "Where anagram-length is the positive, integer length of each anagram [{}]" \
          .format(DEFAULT_ANAGRAM_LENGTH)
      exit()
    anagram_length = int(sys.argv[1])
    if anagram_length <= 0:
      print "Invalid anagram-length of {}".format(sys.argv[1])
      exit(1)

  corpus = Corpus()
  corpus.stdin()

