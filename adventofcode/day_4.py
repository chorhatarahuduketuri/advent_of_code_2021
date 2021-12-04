def read_input():
    return [
        [
            [int(number) for number in line.split()]
            for line
            in number_block.strip().split('\n')
        ]
        if ',' not in number_block else
        [int(number) for number in number_block.split(',')]
        for number_block
        in open('../puzzle_inputs/day_4.txt').read().strip().split('\n\n')
    ]


def first_star(sonar_readings):
    pass


def second_star(sonar_readings):
    pass


def main():
    bingo_game = read_input()
    first_star(bingo_game)
    second_star(bingo_game)


if __name__ == '__main__':
    main()
