"""
Solution for exercise 04.4 MissingInteger
"""


def solution(a):
    max_elem = max(a)
    if max_elem < 1:
        return 1
    source_set = set(a)
    complete_set = set(range(1, max_elem + 1))
    diff = complete_set - source_set
    if diff:
        return min(diff)
    else:
        return max_elem + 1
