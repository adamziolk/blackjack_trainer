import pytest
import random

import setup
import custom_types

@pytest.fixture
def target_cards():
    cards = [
        (1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C'), (6, 'C'), (7, 'C'), (8, 'C'), (9, 'C'), (10, 'C'), (11, 'C'), (12, 'C'), (13, 'C'), (1, 'H'), (2, 'H'), (3, 'H'), (4, 'H'), (5, 'H'), (6, 'H'), (7, 'H'), (8, 'H'), (9, 'H'), (10, 'H'), (11, 'H'), (12, 'H'), (13, 'H'), (1, 'S'), (2, 'S'), (3, 'S'), (4, 'S'), (5, 'S'), (6, 'S'), (7, 'S'), (8, 'S'), (9, 'S'), (10, 'S'), (11, 'S'), (12, 'S'), (13, 'S'), (1, 'D'), (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D'), (6, 'D'), (7, 'D'), (8, 'D'), (9, 'D'), (10, 'D'), (11, 'D'), (12, 'D'), (13, 'D')
        ]
    return [custom_types.Card(v, s) for (v, s) in cards]

@pytest.fixture
def blank_table3():
    p1 = custom_types.Player(id=0)
    p2 = custom_types.Player(id=1)
    p3 = custom_types.Player(id=2)
    return custom_types.Table(players=[p1, p2, p3])



def test_make_shoe__cards(target_cards):
    actual_cards = set(setup.make_shoe(num_decks=3))
    assert all(card in actual_cards for card in target_cards)
    assert all(card in target_cards for card in actual_cards)


def test_initialize_table(blank_table3):
    actual_table = setup.initialize_table(num_players=3)
    assert blank_table3 == actual_table


def test_deal_cards__all():
    target_table = {0: [(12, 'H')], 1: [(10, 'D')], 2: [(1, 'S')], 'dealer': [(3, 'C')]}

    random.seed(0)
    shoe = setup.make_shoe()
    actual_table = setup.initialize_table(num_players=3)
    setup.deal_cards(table=actual_table, shoe=shoe)
    assert target_table == actual_table


# def test_deal_cards__single():
#     target_table = {0: [], 1: [(12, 'H')], 2: [], 'dealer': []}

#     random.seed(0)
#     shoe = setup.make_shoe()
#     actual_table = setup.initialize_table(num_players=3)
#     setup.deal_cards(table=actual_table, shoe=shoe, players=[1])
#     assert target_table == actual_table

#     target_table = {0: [(10, 'D')], 1: [(12, 'H'), (1, 'S')], 2: [], 'dealer': []}
#     setup.deal_cards(table=actual_table, shoe=shoe, players=[0, 1])
#     assert target_table == actual_table