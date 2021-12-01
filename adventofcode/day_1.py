def read_input():
    with open('../puzzle_inputs/day_1.txt') as file:
        return [int(line.strip()) for line in file.read().split()]


def first_star(sonar_readings):
    print(sum([1 if sonar_reading > sonar_readings[i - 1] else 0 for i, sonar_reading in enumerate(sonar_readings)]))


def second_star(sonar_readings):
    print(sum([1 if (i > 2) and (sum(sonar_readings[i - 3:i]) > sum(sonar_readings[i - 4:i - 1])) else 0 for
               i, sonar_reading in enumerate(sonar_readings)]))


def main():
    sonar_readings = read_input()
    first_star(sonar_readings)
    second_star(sonar_readings)


if __name__ == '__main__':
    main()
