#!/usr/bin/env python2.7

import itertools
import re
import sys

ANAGRAM_LENGTH = 2
ONLY_LONGEST = True
MINIMUM_WORD_LENGTH = 4

class Corpus(object):
  def __init__(self):
    self._words = []

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

  def find_matches(self, length=ANAGRAM_LENGTH, only_longest=ONLY_LONGEST):
    matches = []
    data = {}
    key_length = MINIMUM_WORD_LENGTH * length
    for pair in itertools.combinations(self._words, length):
      t = ''.join(sorted(itertools.chain.from_iterable(pair)))


if __name__ == '__main__':
  corpus = Corpus()
  corpus.stdin()
  corpus.find_matches()

