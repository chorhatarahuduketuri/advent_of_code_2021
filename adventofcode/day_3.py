def get_readings():
    with open('../puzzle_inputs/day_3.txt') as file:
        return [line.strip() for line in file.read().split('\n')]


def first_star(readings):
    pass


def second_star(readings):
    pass


def main():
    readings = get_readings()
    first_star(readings)
    second_star(readings)


if __name__ == '__main__':
    main()
