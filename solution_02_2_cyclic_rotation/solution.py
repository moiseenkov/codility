def solution(a, k):
    from collections import deque
    d = deque(a)
    d.rotate(k)
    return list(d)
