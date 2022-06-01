import random
from typing import Optional, Any

if __package__ is None or __package__ == '':
    # uses current directory visibility
    import custom_types
else:
    # uses current package visibility
    import blackjack.custom_types as custom_types


def make_shoe(num_decks: int=1):
    suits = ['C', 'H', 'S', 'D']
    values = range(1, 14)

    cards = [custom_types.Card(v, s) for s in suits for v in values]
    shoe = cards * num_decks
    random.shuffle(shoe)

    return shoe


def initialize_table(players):
    table = custom_types.Table(players=players)

    return table


def deal_player_cards(shoe, players, split_deal=False) -> None:
    for player in players:
        if split_deal:
            player.split_cards.append(shoe.pop())
        else:
            player.cards.append(shoe.pop())

    return


def deal_dealer_cards(table, shoe) -> None:
    table.dealer_cards.append(shoe.pop())

    return
