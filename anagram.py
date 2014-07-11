#!/usr/bin/env python2.7

import re, sys

ord_offset = ord('a')

empty_word = [0] * 26

corpus = { 'words' : [], 'pairs' : {} }

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
  for w in corpus['words']:
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

def iterate_words(corpus, words, position, length, end):
  if length >= 1:
    while position + length < end:
      words.append(corpus['words'][position])
      position += 1
      iterate_words(corpus, words, position, length - 1, end)
      words.pop()
  else:
    print "Check {}".format(words)

for line in sys.stdin:
  line = re.sub('[\W\d]+', ' ', line)
  for s in line.split():
    word = process_word(s)
    if word == None:
      continue

    if not is_duplicate(corpus, word):
      print "{} is {}".format(s, word['data'])
      corpus['words'].append(word)
    else:
      print "{} is a duplicate".format(s)
  iterate_words(corpus, list(), 0, 2, len(corpus['words']))

