"""
Codility exercise 05.3 MinAvgTwoSlice
"""

def solution(a):
    """Returns position of first slice with minimal mean value"""

    def slices_summary(slices):
        """Return slices summary: minimal mean value and slice position"""
        if len(slices) < 1:
            return 0, 0
        min_value = min(slices)
        min_index = slices.index(min_value)
        return min_value, min_index

    # We check only slices containing 2 and 3 elements
    # Proof: https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/
    slice_means_2 = [sum(x) / len(x) for x in zip(a[:-1], a[1:])]
    slice_means_3 = [sum(x) / len(x) for x in zip(a[:-2], a[1:-1], a[2:])]

    _, position = min(slices_summary(slice_means_2), slices_summary(slice_means_3))

    return position
