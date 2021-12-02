def read_input():
    with open('../puzzle_inputs/day_2.txt') as file:
        return [[line.split()[0], int(line.split()[1])] for line in file.read().split('\n') if line]


def main():
    print(read_input())


if __name__ == '__main__':
    main()
