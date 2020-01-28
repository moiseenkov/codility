"""
Codility exercise 05.2 GenomicRangeQuery
"""
from solution_05_2_genomic_range_query.solution import solution


def main():
    """
    Main function calls solution for codility task 05.2
    """
    while True:
        try:
            string = input('Enter string array with following symbols only: A, C, G, T: ')
            p = list(map(int, input('Enter int array: ').strip().split(' ')))
            q = list(map(int, input('Enter int array the same length as the previous: ').strip().
                         split(' ')))
            print(solution(string, p, q))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
