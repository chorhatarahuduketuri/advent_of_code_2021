import pytest

from adventofcode.day_4 import first_star, second_star

day_4_star_1_test_input = [(['something'], 0)]


@pytest.mark.parametrize(["input", "output"], day_4_star_1_test_input)
def test_day_4_star_1(capsys, input, output):
    first_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output


day_4_star_2_test_input = [(['something'], 0)]


@pytest.mark.parametrize(["input", "output"], day_4_star_2_test_input)
def test_day_4_star_2(capsys, input, output):
    second_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output
