#!/usr/local/bin/python3
# Advanced python
# Assignment : 12 - CPython
# Desc : Write a universal program that expects its command line arguments to contain the absolute path to any program, followed by its arguments. The wrapper should run that program and report its exit value.

#########
####  IMPORTANT
####  shebang is included !
####  i suggest 'filename.py Python -V' in command line
#########

import sys, subprocess
# command line arguments contain the absolute path to ay program followed by its arguments
try:
    absolutepath = sys.argv[1]
    argument = sys.argv[2]

    print ('This is your program path : ',absolutepath)
    print('This is your argument : ', argument, '\n')
except:
    print('something went wron... check your input and try again')

try:
    # wrapper should run the program
    command = [absolutepath, argument]
    result = subprocess.run(command, stdout=subprocess.PIPE, timeout=10**-1)
    print(' This is your output : \n')
    # and report its exit value..
    print(result.stdout)
except:
    print('something went wrong... check your input and try again')
