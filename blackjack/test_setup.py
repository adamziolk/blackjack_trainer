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
def player_list():
    p0 = custom_types.Player(id=0)
    p1 = custom_types.Player(id=1)
    p2 = custom_types.Player(id=2)
    return [p0, p1, p2]

@pytest.fixture
def blank_table3(player_list):
    return custom_types.Table(players=player_list)



def test_make_shoe__cards(target_cards):
    actual_cards = set(setup.make_shoe(num_decks=3))
    assert all(card in actual_cards for card in target_cards)
    assert all(card in target_cards for card in actual_cards)


def test_initialize_table(blank_table3, player_list):
    actual_table = setup.initialize_table(players=player_list)
    assert blank_table3 == actual_table


def test_deal_player_cards__all(blank_table3, player_list):
    target_table = blank_table3
    target_table.players[0].cards = [custom_types.Card(12, 'H')]
    target_table.players[1].cards = [custom_types.Card(10, 'D')]
    target_table.players[2].cards = [custom_types.Card(1, 'S')]

    random.seed(0)
    shoe = setup.make_shoe()
    actual_table = setup.initialize_table(players=player_list)
    setup.deal_player_cards(table=actual_table, shoe=shoe)
    assert target_table == actual_table


def test_deal_player_cards__single(blank_table3, player_list):
    target_table = blank_table3
    target_table.players[1].cards = [custom_types.Card(12, 'H')]

    random.seed(0)
    shoe = setup.make_shoe()
    actual_table = setup.initialize_table(players=player_list)
    setup.deal_player_cards(table=actual_table, shoe=shoe, player=actual_table.players[1])
    assert target_table == actual_table

    target_table.players[0].cards = [custom_types.Card(10, 'D')]
    target_table.players[1].cards = [custom_types.Card(12, 'H'), custom_types.Card(1, 'S')]
    setup.deal_player_cards(table=actual_table, shoe=shoe, player=actual_table.players[0])
    setup.deal_player_cards(table=actual_table, shoe=shoe, player=actual_table.players[1])

    assert target_table == actual_table


def test_deal_dealer_cards(blank_table3, player_list):
    target_table = blank_table3
    target_table.dealer_cards = [custom_types.Card(12, 'H')]

    random.seed(0)
    shoe = setup.make_shoe()
    actual_table = setup.initialize_table(players=player_list)
    setup.deal_dealer_cards(table=actual_table, shoe=shoe)
    assert target_table == actual_table

    target_table.dealer_cards = [custom_types.Card(12, 'H'), custom_types.Card(10, 'D')]
    setup.deal_dealer_cards(table=actual_table, shoe=shoe)
    assert target_table == actual_table


