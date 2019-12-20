def solution(a):
    max_elem = max(a)
    if max_elem != len(a):
        return 0
    data_set = set(a)
    complete_set = set(range(1, max_elem + 1))
    return 1 if data_set == complete_set else 0
