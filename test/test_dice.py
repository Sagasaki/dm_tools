import pytest
from src.dice import Dice


def test_basic_roll():
    x = Dice()
    assert 1 <= x.basic_roll(20) <= 20
    with pytest.raises(TypeError):
        x._roll('test')
    