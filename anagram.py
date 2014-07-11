#!/usr/bin/env python2.7

import re
import sys

ORD_OFFSET = ord('a')
ANAGRAM_LENGTH = 2
MINIMUM_WORD_LENGTH = 4

class Word(object):
  def __init__(self, word):
    self.length = len(word)
    assert(self.length >= MINIMUM_WORD_LENGTH)
    self.original = word
    self.composition = [0] * 26
    for char in word.lower():
      self.composition[ord(char) - ORD_OFFSET] += 1

  def __len__(self):
    return self._length

class Pair(object):
  def __init__(self, words):
    self._length = len(words)
    assert(self._length == ANAGRAM_LENGTH)
    self.words = []
    self.compare_string = ''
    for i in range(26):
      for word in words:
        self.compare_string += chr(i + ORD_OFFSET) * word.composition[i]
    for word in words:
      self.words.append(word.original)

  def __str__(self):
    return str(self.words)

  def __len__(self):
    return self._length

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
    self._iterate_word_pairs(list(), 0, ANAGRAM_LENGTH, len(self._words))
    self._find_matches()

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

def process_words_into_pairs(corpus, words):
  if not length in corpus['pairs']:
    corpus['pairs'][length] = {}
  if not compare in corpus['pairs'][length]:
    corpus['pairs'][length][compare] = list()
  corpus['pairs'][length][compare].append(pair)

corpus = Corpus()
corpus.process()
for match in corpus.matches:
  print "Found Match: {}".format(match)

