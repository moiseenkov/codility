from solution_02_1_odd_occurrences_in_array.solution import solution


def main():
    while True:
        try:
            message = 'Enter array of positive integers, where only one of them doesn\'t have pair 1 2 1 2 3: '
            numbers = list(map(int, input(message).strip().split(' ')))
            negative_numbers = [value for value in numbers if value < 0]
            if negative_numbers:
                print(f'Wrong input! There are negative numbers: {negative_numbers}. Try again')
                continue
            print(solution(numbers))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
