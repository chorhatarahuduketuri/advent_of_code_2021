import pytest

from day_3 import first_star, second_star

day_3_star_1_test_input = [
    (['00100',
      '11110',
      '10110',
      '10111',
      '10101',
      '01111',
      '00111',
      '11100',
      '10000',
      '11001',
      '00010',
      '01010'],
     198)
]


@pytest.mark.parametrize(["input", "output"], day_3_star_1_test_input)
def test_day_3_star_1(capsys, input, output):
    first_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output


day_3_star_2_test_input = [
    (['00100',
      '11110',
      '10110',
      '10111',
      '10101',
      '01111',
      '00111',
      '11100',
      '10000',
      '11001',
      '00010',
      '01010'],
     230)
]


@pytest.mark.parametrize(["input", "output"], day_3_star_2_test_input)
def test_day_3_star_2(capsys, input, output):
    second_star(input)
    captured = capsys.readouterr()
    assert int(captured.out) == output
