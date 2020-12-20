#!/usr/local/bin/python3
# 10 - profiling
import cProfile
import pstats
from functools import reduce

def comprehension():
    print(reduce(lambda a, x: a + x.count(x[::-1]), map(lambda word: word.strip(), open('english')), 0))

def structured():
    fhand = open('english')
    count = 0
    for line in fhand:
        line = line.strip()
        rev = line[::-1]
        if (line == rev):
            count = count + 1
    print(count)
    return count

stats = pstats.Stats(cProfile.run('structured()'))
stats.sort_stats("tottime")
stats.print_stats(10)

cProfile.run('comprehension()')
