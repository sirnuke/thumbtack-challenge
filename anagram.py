#!/usr/bin/env python2.7

import re, sys

ord_offset = ord('a')

letter_bits = []

for i in range(0, ord('z') - ord_offset):
  letter_bits.append(2**i)

for line in sys.stdin:
  line = re.sub('[\W\d]+', ' ', line)
  for word in line.split():
    print word

