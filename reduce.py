#!/usr/bin/env python

from operator import itemgetter
import sys


word2count = {}



for line in sys.stdin:
   
    line = line.strip()

    word, count = line.split('\t', 1)
  
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:

        pass


for key in word:
	word2count[key] = word2count.get(key, 0) + 1

sorted_word2count = sorted(word2count.items(), key= lambda x:x[1], reverse = True)


for word, count in sorted_word2count:
    print ('%s\t%s'% (word, count))