# formula = a^2 + b^2 = c^2
import pytest
from unittest.mock import MagicMock
from ..app import Matematical, Pitagoras


def my_squared_results(parameter):
    if parameter == 3:
        return 9
    return 16

def _test_matematical_number_squared():
    number = 3
    expected_result = 9
    matemathical = Matematical()

    result = matemathical.squared(number)

    assert expected_result == result

def _test_matematical_number_plus():
    a = 3
    b = 2

    expected_result = 5
    matemathical = Matematical()

    result = matemathical.plus(a, b)

    assert expected_result == result

def test_pitagoras(a, b):
    
    
    expected_result = 5
    fake_matematical = MagicMock()
    fake_matematical.squared = MagicMock(side_effect = my_squared_results)
    pitagoras = Pitagoras(fake_matematical)

    result = pitagoras.run(a, b)

    assert expected_result == result


