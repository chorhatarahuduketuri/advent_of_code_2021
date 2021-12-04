def get_readings():
    with open('../puzzle_inputs/day_3.txt') as file:
        return [line.strip() for line in file.read().split('\n') if line]


def count_zeros_and_ones(readings, as_string=False):
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
    if as_string:
        counted = [[str(x) for x in count] for count in counted]
    return counted


def first_star(readings):
    counted = count_zeros_and_ones(readings)
    gamma = int(''.join([str(count[0]) for count in counted]), 2)
    epsilon = int(''.join([str(count[1]) for count in counted]), 2)
    print(gamma * epsilon)


def filter_readings_for_rating(counted, readings, ind):
    ratings_data = readings.copy()
    for i in range(len(counted)):
        if len(ratings_data) == 1:
            break
        else:
            count = count_zeros_and_ones(ratings_data, True)
            ratings_data = [ratings_datum for ratings_datum in ratings_data if
                            (ratings_datum[i] == (count[i][ind] if count[i][0] != count[i][1] else str(ind)))]
    return ratings_data


def second_star(readings):
    counted = count_zeros_and_ones(readings, True)
    oxygen_generator_rating = filter_readings_for_rating(counted, readings, 1)
    co2_scrubber_rating = filter_readings_for_rating(counted, readings, 0)
    oxygen_generator_rating = int(oxygen_generator_rating[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating[0], 2)
    print(oxygen_generator_rating * co2_scrubber_rating)


def main():
    readings = get_readings()
    first_star(readings)
    second_star(readings)


if __name__ == '__main__':
    main()
