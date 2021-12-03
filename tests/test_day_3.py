import pytest

from day_3 import first_star, second_star

day_3_star_1_test_input = [(['something'], 198)]


@pytest.mark.parametrize(["input", "output"], day_3_star_1_test_input)
def test_day_3_star_1(capsys, input, output):
    first_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output


day_3_star_2_test_input = [([''], 0)]


@pytest.mark.parametrize(["input", "output"], day_3_star_2_test_input)
def test_day_3_star_2(capsys, input, output):
    second_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output
