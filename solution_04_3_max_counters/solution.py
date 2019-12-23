"""
Solution for exercise 04.3 MaxCounters
"""


def solution(n, a):
    """
    For more information see test_results.pdf
    """
    counters = [0 for _ in range(n)]
    lower = 0
    higher = 0
    for command in a:
        i = command - 1
        if command < n + 1:
            value = max(counters[i], lower) + 1
            higher = max(higher, value)
            counters[i] = value
        else:
            lower = higher
    for i in range(n):
        if counters[i] < lower:
            counters[i] = lower
    return counters
