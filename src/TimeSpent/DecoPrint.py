# measure speed using print and decorator
from functools import wraps
import time

def timeFn(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        time_spent = t2 - t1
        print(f'@timeFn: {fn.__name__} spent {time_spent} seconds')
        return result
    return wrap


@timeFn
def sleep1sFn():
    time.sleep(1)
