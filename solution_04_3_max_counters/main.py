"""
Codility exerciece 04.3 MacCounters
"""
from solution_04_3_max_counters.solution import solution


def main():
    """
    Main function calls solution for codility task 04.3
    """
    while True:
        try:
            number = int(input('Enter integer n: '))
            array = list(map(int, input('Enter int array: ').strip().split(' ')))
            print(solution(number, array))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
