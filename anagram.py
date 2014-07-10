#!/usr/bin/env python2.7

import re, string, sys

base_word = {}

for c in string.lowercase:
  base_word[c] = 0

for line in sys.stdin:
  line = re.sub('[\W\d]+', ' ', line)
  for word in line.split():
    if len(word) < 4:
      continue
    word = word.lower()
    data = base_word.copy()
    for c in word:
      data[c] += 1
    print "{} is {}".format(word, data)

