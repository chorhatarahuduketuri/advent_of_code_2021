import pytest

import day_1

day_1_star_1 = [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)]


@pytest.mark.parametrize(["input", "output"], day_1_star_1)
def test_day_1_star_1(capsys, input, output):
    day_1.first_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == 7


@pytest.mark.parametrize(["input", "output"], day_1_star_1)
def test_day_1_star_2(capsys, input, output):
    day_1.second_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == 5