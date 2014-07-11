#!/usr/bin/env python2.7

import re
import sys

ORD_OFFSET = ord('a')
ANAGRAM_LENGTH = 10
MINIMUM_WORD_LENGTH = 4

class Word(object):
  def __init__(self, word):
    assert(len(word) >= MINIMUM_WORD_LENGTH)
    self.original = word
    self.composition = [0] * 26
    for char in word.lower():
      self.composition[ord(char) - ORD_OFFSET] += 1

class Pair(object):
  def __init__(self, words):
    assert(len(words) == ANAGRAM_LENGTH)
    self.words = []
    self.compare_string = ''
    for i in range(26):
      for word in words:
        self.compare_string += chr(i + ORD_OFFSET) * word.composition[i]
    for word in words:
      self.words.append(word.original)

class Match(object):
  def __init__(self, pairs):
    assert(len(pairs) > 1)
    self.pairs = []
    for pair in pairs:
      self.pairs.append(pair.words)

  def __str__(self):
    res = ""
    for i,pair in enumerate(self.pairs):
      if i > 0:
        res += "; "
      for j,v in enumerate(pair):
        if j > 0:
          res += ","
        res += v
    return res

class Corpus(object):
  def __init__(self):
    self._words = []
    self._pairs = {}
    self.matches = []

  def process(self):
    for line in sys.stdin:
      line = re.sub('[\W\d]+', ' ', line)
      for w in line.split():
        self._add_word(w)
    print "Done adding words"
    self._iterate_word_pairs(list(), 0, ANAGRAM_LENGTH, len(self._words))
    print "Done getting pairs"
    self._find_matches()
    print "Done finding matches"

  def _add_word(self, word):
    if len(word) < MINIMUM_WORD_LENGTH:
      return
    for w in self._words:
      if w.original == word:
        return
    self._words.append(Word(word))

  def _iterate_word_pairs(self, words, position, length, end):
    if length > 0:
      while position + length < end:
        words.append(self._words[position])
        position += 1
        self._iterate_word_pairs(words, position, length - 1, end)
        words.pop()
    else:
      p = Pair(words)
      if not p.compare_string in self._pairs:
        self._pairs[p.compare_string] = []
      self._pairs[p.compare_string].append(p)

  def _find_matches(self):
    for i,row in self._pairs.iteritems():
      if len(row) > 1:
        self.matches.append(Match(row))

corpus = Corpus()
corpus.process()
for match in corpus.matches:
  print match

