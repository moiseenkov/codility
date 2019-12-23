"""
Codility exerciece 04.4 MissingInteger
"""
from solution_04_4_missing_integer.solution import solution


def main():
    """
    Main function calls solution for codility task 04.4
    """
    while True:
        try:
            array = list(map(int, input('Enter int array: ').strip().split(' ')))
            print(solution(array))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
