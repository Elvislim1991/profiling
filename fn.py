#!/usr/bin/env python3

import random
import time

from src.TimeSpent.DecoPrint import timeFn

@timeFn
def complexFn1():
    random.seed(100)

    def act1():
        time_elapsed = random.randint(1, 5)
        print(f'{time_elapsed} s for act1')
        time.sleep(time_elapsed)

    def act2():
        time_elapsed = random.randint(1, 5)
        print(f'{time_elapsed} s for act1')
        time.sleep(time_elapsed)

    def act3():
        time_elapsed = random.randint(1, 5)
        print(f'{time_elapsed} s for act1')
        time.sleep(time_elapsed)
        
    act1()
    act2()
    act3()


if __name__ == '__main__':
    complexFn1()
