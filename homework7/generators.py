import random
import math
from datetime import datetime, timedelta


def all_even_numbers():
    x = 0
    while x < 100:
        yield x
        x += 2


def random_increasing_number():
    num = 2**64 # since int('inf') is not present, just some number
    current_num = random.randint(-num, num)
    while True:
        yield current_num
        current_num = random.randint(current_num, current_num+num)


def next_day():
    current_day = datetime.today().date()
    while True:
        yield current_day
        current_day += timedelta(days=1)
