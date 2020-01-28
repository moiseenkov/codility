"""
Solution for task 05.2 GenomicRangeQuery
"""


def solution(s, p, q):
    """"Solution for task 05.2 GenomicRangeQuery"""
    a_prefix = [0 for _ in range(len(s) + 1)]
    c_prefix = a_prefix.copy()
    g_prefix = a_prefix.copy()
    for i, nucleotide in enumerate(s):
        a_prefix[i + 1] = a_prefix[i] + (1 if nucleotide == 'A' else 0)
        c_prefix[i + 1] = c_prefix[i] + (1 if nucleotide == 'C' else 0)
        g_prefix[i + 1] = g_prefix[i] + (1 if nucleotide == 'G' else 0)
    result = []
    for left, right in zip(p, q):
        if a_prefix[right + 1] - a_prefix[left] > 0:
            result.append(1)
        elif c_prefix[right + 1] - c_prefix[left] > 0:
            result.append(2)
        elif g_prefix[right + 1] - g_prefix[left] > 0:
            result.append(3)
        else:
            result.append(4)
    return result
