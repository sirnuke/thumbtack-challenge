#!/usr/bin/env python2.7

import re, string, sys


ord_offset = ord('a')

empty_word = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

corpus = []

def process_word(s):
  length = len(s)
  if length < 4:
    return None
  s = s.lower()
  word = { "length" : length, "original" : s, "data" : list(empty_word) }
  for c in s:
    word['data'][ord(c) - ord_offset] += 1

  return word


def is_duplicate(corpus, word):
  for w in corpus:
    if w['original'] == word['original']:
      return True
  return False

def create_compare_string(words):
  compare = ""
  for i in range(26):
    char = chr(i + ord_offset)
    for word in words:
      compare += char*word["data"][i]
  return compare

for line in sys.stdin:
  line = re.sub('[\W\d]+', ' ', line)
  for s in line.split():
    word = process_word(s)
    if word == None:
      continue

    if not is_duplicate(corpus, word):
      print "{} is {}".format(s, word['data'])
      corpus.append(word)
    else:
      print "{} is a duplicate".format(s)

