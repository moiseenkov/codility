"""
Codility exercise 05.1 PassingCars
"""
from solution_05_1_passing_cars.solution import solution


def main():
    """
    Main function calls solution for codility task 05.1
    """
    while True:
        try:
            array = list(map(int, input('Enter int array with 0 or 1: ').strip().split(' ')))
            print(solution(array))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
