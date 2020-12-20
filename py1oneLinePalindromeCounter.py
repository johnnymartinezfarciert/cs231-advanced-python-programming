# cs231 : Python Advanced
# Assignment : 1
# Author : John Martinez
# January 31, 2019 (baby Marley Jude's birthday)
#
# one line program that prints the number of palindromes
# in /users/abrick/resources/english
from functools import reduce
def fast():
    print(reduce(lambda a, x: a + x.count(x[::-1]), map(lambda word: word.strip(), open('english')), 0))

def slow():
    fhand = open('english')
    count = 0
    for line in fhand:
        line = line.strip()
        rev = line[::-1]
        if (line == rev):
            count = count + 1
    print(count)
    return count

slow()
fast()
