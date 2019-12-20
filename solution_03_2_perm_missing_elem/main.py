from solution_03_2_perm_missing_elem.solution import solution


def main():
    while True:
        try:
            array = list(map(int, input('Enter array of integers from 1 to N+1 '
                                        'where one element missed: ').strip().split(' ')))
            print(solution(array))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
