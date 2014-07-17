#!/usr/bin/env python2.7

import itertools
import re
import sys

ANAGRAM_LENGTH = 2
MINIMUM_WORD_LENGTH = 4
KEY_LENGTH = 1

class AnagramPairs(object):
  def __init__(self):
    self._words = []

  def stdin(self):
    for word in re.sub('[\W\d]+', ' ', sys.stdin.read()).split():
      self.add_word(word)

  def add_word(self, word):
    if len(word) < MINIMUM_WORD_LENGTH: return
    word = word.lower()
    for w in self._words:
      if w == word: return
    self._words.append(word)

  def find_matches(self, anagram_length=ANAGRAM_LENGTH):
    matches = []
    data = {}
    match_length = 2
    for pair in itertools.combinations(self._words, anagram_length):
      chars = ''.join(sorted(''.join(pair)))
      key = chars[:KEY_LENGTH]
      pair = set(pair)
      if not key in data: data[key] = {}
      if not chars in data[key]: data[key][chars] = []

      if self._is_unique(pair, data[key][chars]):
        data[key][chars].append(pair)
        num_matches = len(data[key][chars])
        if num_matches >= match_length:
          if num_matches > match_length:
            match_length = num_matches
            matches = []
          matches.append(chars)

    print "(length is {})".format(match_length)

    for chars in matches:
      print '; '.join(map(lambda x: ', '.join(x), data[chars[:KEY_LENGTH]][chars]))

  def _is_unique(self, pair, matches):
    for possible in matches:
      if len(possible & pair) != 0:
        return False
    return True

if __name__ == '__main__':
  anagrams = AnagramPairs()
  anagrams.stdin()
  anagrams.find_matches()

