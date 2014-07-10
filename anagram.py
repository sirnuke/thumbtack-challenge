#!/usr/bin/env python2.7

import re, string, sys


ord_offset = ord('a')

base_word = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

for line in sys.stdin:
  line = re.sub('[\W\d]+', ' ', line)
  for word in line.split():
    if len(word) < 4:
      continue
    word = word.lower()
    data = list(base_word)
    for c in word:
      data[ord(c) - ord_offset] += 1
    print "{} is {}".format(word, data)

