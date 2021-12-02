import pytest

from day_2 import first_star

day_2_star_1_test_input = [([('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)], 150)]


@pytest.mark.parametrize(["input", "output"], day_2_star_1_test_input)
def test_day_2_star_1(capsys, input, output):
    first_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output
