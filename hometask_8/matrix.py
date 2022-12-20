import time
import functools
import multiprocessing as mp

def time_dec(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        return time.time() - start_time

    return wrapper

