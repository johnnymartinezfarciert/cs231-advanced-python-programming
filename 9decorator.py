#Decorate print() such that (A) it refuses to print anything under ten
# ten characters long and (B) only five calls are allowed, and
# demonstrate these restrictions when the program is run
import functools

import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


#This function decorates the one passed in as an argument
@count_calls
def limit_print(action):

    # Define and return a new function containing the decorated action
    def inner(string):
        if len(string) < 10:
            #string= 'String must be at least ten characters long'
            pass
        elif 1 > 5:
            #string = 'reached the limit of print, only 5 calls allowed'
            pass
        else:
            return action(string)
    return inner

#@add_logging
#def print(string):
#    print(string)

#call the original version, decorate it, and call again

print('butt')
print('hello my friend')
print('testing testing testing')
print('i want to rock n roll all night and party everyday')
print('we want pizza give us pizza')
print('nachos are my favorite')
print('this should not print')
print('\n_______________DECOCORATOR________________\n')


print=limit_print(print)
print('butt')
print('hello my friend')
print('testing testing testing')
print('i want to rock n roll all night and party everyday')
print('we want pizza give us pizza')
print('nachos are my favorite')
print('this should not print')
print('fuck still not working')
print('asdflakj alksdjfalksd aflskdjf ')
