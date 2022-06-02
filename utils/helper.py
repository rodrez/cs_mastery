from functools import wraps
from time import time
import random


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'Function: {f.__name__}  Took: {round(te-ts, 4)} sec')
        return result
    return wrap


def large_array(length):
    return [ random.randint(0, 10) for _ in range(length)] + [1]