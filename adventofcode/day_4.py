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


def mark_board(board, number):
    return [[num if num != number else None for num in row] for row in board]


def check_board_for_line(board):
    columns = [False, False, False, False, False]
    for row in board:
        if not any(row):
            return True
        for i, column in enumerate(row):
            if column:
                columns[i] = True
    if False in columns:
        return True
    return False


def score_board(board, last_number):
    return sum(filter(None, [number for row in board for number in row])) * last_number


def first_star(bingo_game):
    numbers = bingo_game[0]
    boards = bingo_game[1:]
    for number in numbers:
        for i, board in enumerate(boards):
            boards[i] = mark_board(boards[i], number)
            if check_board_for_line(boards[i]):
                print(score_board(boards[i], number))
                return


def second_star(bingo_game):
    numbers = bingo_game[0]
    boards = bingo_game[1:]
    finished_boards = []
    last_number = -1
    last_score = -1
    for number in numbers:
        for i, board in enumerate(boards):
            if i not in finished_boards:
                boards[i] = mark_board(boards[i], number)
                if check_board_for_line(boards[i]):
                    finished_boards.append(i)
                    last_number = number
                    last_score = score_board(boards[i], number)
    print(last_score)


def main():
    bingo_game = read_input()
    first_star(bingo_game)
    second_star(bingo_game)


if __name__ == '__main__':
    main()
