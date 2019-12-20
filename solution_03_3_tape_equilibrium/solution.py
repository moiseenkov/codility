def solution(a):
    sum_left = sum(a[:1])
    sum_right = sum(a[1:])
    result = abs(sum_left - sum_right)
    for elem in a[1:-1]:
        sum_left += elem
        sum_right -= elem
        result = min(result, abs(sum_left - sum_right))
    return result
