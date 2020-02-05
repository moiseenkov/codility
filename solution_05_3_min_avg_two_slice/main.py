"""
Codility exercise 05.3 MinAvgTwoSlice
"""
from solution_05_3_min_avg_two_slice.solution import solution


def main():
    """
    Main function calls solution for codility task 05.3
    """
    while True:
        try:
            a = list(map(int, input('Enter int array: ').strip().split(' ')))
            print(solution(a))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
