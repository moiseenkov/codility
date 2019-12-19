from solution_03_1_frog_jmp.solution import solution


def main():
    while True:
        try:
            parameters = list(map(int, input('Enter X, Y, D: ').strip().split(' ')))
            print(solution(*parameters))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
