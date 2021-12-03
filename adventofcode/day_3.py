def get_readings():
    with open('../puzzle_inputs/day_3.txt') as file:
        return [line.strip() for line in file.read().split('\n')]


def first_star(readings):
    counters = dict()
    for i in range(len(readings[0])):
        counters[i] = [0, 0]
    for reading in readings:
        for i, bit in enumerate(reading):
            if bit == '0':
                counters[i][0] += 0
                counters[i][1] += 1
            else:
                counters[i][0] += 1
                counters[i][1] += 0
    counted = [[counter.index(max(counter)), counter.index(min(counter))] for k, counter in counters.items()]
    gamma = int(''.join([str(count[0]) for count in counted]), 2)
    epsilon = int(''.join([str(count[1]) for count in counted]), 2)
    print(gamma * epsilon)


def second_star(readings):
    pass


def main():
    readings = get_readings()
    first_star(readings)
    second_star(readings)


if __name__ == '__main__':
    main()
