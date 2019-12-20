from solution_04_2_frog_river_one.solution import solution


def main():
    while True:
        try:
            x = int(input('Enter integer x: '))
            array = list(map(int, input('Enter int array: ').strip().split(' ')))
            print(solution(x, array))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
