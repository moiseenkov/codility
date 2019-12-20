def solution(a):
    n = len(a)
    complete_set = set(range(1, n + 2))
    current_set = set(a)
    missing = complete_set - current_set
    return missing.pop()
