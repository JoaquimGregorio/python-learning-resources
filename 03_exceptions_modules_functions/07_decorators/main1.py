from typing import Callable
from time import time, sleep


def velocity(func: Callable):
    def intern(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = int((end_time - start_time) * 1000)
        print(f"The function {func.__name__} took {total_time}ms to be executed.")
        return result

    return intern


@velocity
def delay():
    for i in range(5):
        print(i)
        sleep(1)


delay()
