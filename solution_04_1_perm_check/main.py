from solution_04_1_perm_check.solution import solution


def main():
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
