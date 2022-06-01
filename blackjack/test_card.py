import pytest

import custom_types

def test_card__true_value():
    c1 = custom_types.Card(10, 'S')
    c2 = custom_types.Card(12, 'H')
    c3 = custom_types.Card(1, 'D')

    assert c1.value != c2.value
    assert c1.true_value == c2.true_value
    assert c3.true_value == 11