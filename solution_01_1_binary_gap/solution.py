def solution(n):
    binary_string = str(bin(n))[2:]
    binary_gaps = binary_string.strip('0').split('1')
    return max(list(map(len, binary_gaps)))
