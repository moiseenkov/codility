from solution_01_1_binary_gap.solution import solution


def main():
    while True:
        try:
            n = int(input('Put positive integer number: '))
            if n < 0:
                print(f'Wrong input! {n} should be positive. Try again')
                continue

            print(f'Length of longest binary gap is: {solution(n)}')
        except ValueError as ex:
            print(f'Wrong input: {ex}. Try again')
            continue


if __name__ == '__main__':
    main()
