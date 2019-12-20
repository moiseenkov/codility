from solution_03_3_tape_equilibrium.solution import solution


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
