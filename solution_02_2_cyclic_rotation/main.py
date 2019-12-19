from solution_02_2_cyclic_rotation.solution import solution


def main():
    while True:
        try:
            numbers = list(map(int, input('Enter array of integers: ').strip().split(' ')))
            rotation = int(input('Enter rotation number: '))
            print(solution(numbers, rotation))
        except ValueError as ex:
            print(f'Wring input! {ex}. Try again.')
            continue
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()
