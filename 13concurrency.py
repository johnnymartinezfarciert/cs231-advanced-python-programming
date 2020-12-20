# Demonstrate race condition with many unsafe calls.
# import os, threading
#
# def unsafe():
#     global value
#     found = value
#     with open(os.devnull, 'w') as null:
#         busywork = print(found*str(found), file=null)
#     value = found - 1
#
# value = 10**3
# print(value)
# for _ in range(value):
#     threading.Thread(target=unsafe).start()
#
# print(value)


# Functional calculation of ten logarithms.
import concurrent.futures, math
inputs = range(1,10)
pool = concurrent.futures.ThreadPoolExecutor()
print(list(pool.map(math.log, inputs)), list (zip(inputs, pool.map(math.log, inputs))))


def try_utf(fp):
    f = open(fp, 'rb')
    data = f.read()
    try:
        data.decode('utf-8')
        return 'IS UTF-8'
    except UnicodeDecodeError :
        return 'NOT UTF-8'


# def try_utf(data):
#     try:
#         return data.decode('utf-8')
#     except UnicodeDecodeError :
#         return None



def check_encoding(fp):
    f = open(fp, 'rb')
    data = f.read()
    udata = try_utf(data)
    if udata is None:
        return 'Not UTF-8'
    else:
        return ' IS UTF-8'


fps = ['elves.txt', '9dec.py']

pool = concurrent.futures.ThreadPoolExecutor()
# print(list(pool.map(try_utf, fps)), list(zip(fps, pool.map(check_encoding, fps))))
print(list(zip(fps, pool.map(try_utf, fps))))

import os
fps = os.listdir()
print(list(zip(fps, pool.map(try_utf, fps))))
