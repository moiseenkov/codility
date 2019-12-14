def solution(a):
    from collections import defaultdict
    d = defaultdict(lambda: -1)
    for number in a:
        value = d[number]
        d[number] = value * (-1)

    for key, value in d.items():
        if value > 0:
            return key

    return None
