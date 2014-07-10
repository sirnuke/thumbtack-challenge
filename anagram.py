#!/usr/bin/env python2.7

import re, string, sys


ord_offset = ord('a')

empty_word = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

corpus = []

def is_duplicate(corpus, word):
  for w in corpus:
    if w['original'] == word['original']:
      return True
  return False

for line in sys.stdin:
  line = re.sub('[\W\d]+', ' ', line)
  for s in line.split():
    if len(s) < 4:
      continue
    s = s.lower()
    word = { "length" : len(s), "original" : s, "data" : list(empty_word) }
    for c in s:
      word['data'][ord(c) - ord_offset] += 1

    if not is_duplicate(corpus, word):
      print "{} is {}".format(s, word['data'])
      corpus.append(word)
    else:
      print "{} is a duplicate".format(s)

