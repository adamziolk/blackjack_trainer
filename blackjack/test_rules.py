import pytest

import custom_types
import rules

@pytest.fixture
def player_list():
    p0 = custom_types.Player(id=0)
    p1 = custom_types.Player(id=1)
    p2 = custom_types.Player(id=2)
    return [p0, p1, p2]


def test_rules__check_bust(player_list):
    player_list[0].cards = [custom_types.Card(10, 'D'), custom_types.Card(5, 'S')]
    assert rules.check_bust(player_list[0]) == False

    player_list[1].cards = [custom_types.Card(13, 'D'), custom_types.Card(10, 'S'), custom_types.Card(1, 'H'), custom_types.Card(1, 'S')]
    assert rules.check_bust(player_list[1]) == True