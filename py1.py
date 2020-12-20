from functools import reduce
w = map(lambda word: word[::-1], open('english'))
print(w)


word_count = reduce(lambda a, x: a + x.count(x[::-1]), map(lambda word: word.strip(), open('english')), 0)
#i created a map of the reversed words
#how do i compare two maps
print(word_count)

f_count = reduce(lambda a, x: a + x.count(x),
filter(lambda word: str(word[::-1]) == str(word), open('english')), 0)
print(f_count)
