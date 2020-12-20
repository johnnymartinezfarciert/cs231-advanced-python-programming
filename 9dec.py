#!/usr/local/bin/python3
# Advanced Python
# 9 Decorators
# Decorate print() such that (A) it refuses to print anything under ten
# ten characters long and (B) only five calls are allowed, and
# demonstrate these restrictions when the program is run
import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        if len(*args) < 10:
            func('string must be at least ten characters')
            pass
        elif wrapper_count_calls.num_calls > 5:
            func('exceeded number of allowed callsrm')
            pass
        else:
            return func(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}"), func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

print = count_calls(print)
print('butt')
print('hello my friend')
print('testing testing testing')
print('i want to rock n roll all night and party everyday')
print('we want pizza give us pizza')
print('nachos are my favorite')
print('this should not print')
print('this too should not print')
