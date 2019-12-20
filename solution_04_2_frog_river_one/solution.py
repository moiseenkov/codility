def solution(x, a):
    way = set(range(1, x + 1))
    path = set()
    for i, leaf in enumerate(a):
        path.add(leaf)
        if path == way:
            return i
    return -1
