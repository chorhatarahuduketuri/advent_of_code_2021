def read_input():
    with open('../puzzle_inputs/day_2.txt') as file:
        return [[line.split()[0], int(line.split()[1])] for line in file.read().split('\n') if line]


def first_star(commands):
    position = [0, 0]  # [horizontal, vertical]
    for command in commands:
        if command[0] == 'forward':
            position[0] += command[1]
        if command[0] == 'down':
            position[1] += command[1]
        if command[0] == 'up':
            position[1] -= command[1]
    answer = position[0] * position[1]
    print(answer)


def second_star(commands):
    position = [0, 0, 0]  # [horizontal, vertical, aim]
    for command in commands:
        if command[0] == 'forward':
            position[0] += command[1]
            position[1] += command[1] * position[2]
        if command[0] == 'down':
            position[2] += command[1]
        if command[0] == 'up':
            position[2] -= command[1]
    answer = position[0] * position[1]
    print(answer)


def main():
    commands = read_input()
    first_star(commands)
    second_star(commands)


if __name__ == '__main__':
    main()
