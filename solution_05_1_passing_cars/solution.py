"""
Solution for exercise 05.1 PassingCars
"""
from itertools import accumulate


def solution(a):
    suffix_sum = list(accumulate(reversed(a)))
    counter = 0
    prev = suffix_sum[0]
    for value in suffix_sum[1:]:
        if value == prev:
            counter += prev
        else:
            prev = value
        if counter > 1000000000:
            return -1
    return counter
