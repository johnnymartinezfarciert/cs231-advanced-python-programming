#!/usr/local/bin/python3
# CS231 - Advanced Python
# Assignment : Generators II
# Author: John Martinez
# Desc: program that rewraps text from the filename passed so that it
#     fits an 80 column window without breaking any words. Use a
#     generator that yields the next line of text, containing as many #     words as possible
#

import sys

#### Generator ####
def line_gen(filename):
    import textwrap

    f = open(filename)
    for line in f:
        # Multiplexing generation: The variant yield from introduces yet another layer of abstraction,
        #for yielding another iterable generator
        yield from textwrap.wrap(width=80, text=line)
#### END OF GENERATOR ####

filename = sys.argv[1]

gen = line_gen(filename)

for line in gen:
    print(line)
