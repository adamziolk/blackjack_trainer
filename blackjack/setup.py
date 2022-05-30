import random
from typing import Optional, Any

from custom_types import Shoe, Table, Card, Player


def make_shoe(num_decks: int=1) -> Shoe:
    suits = ['C', 'H', 'S', 'D']
    values = range(1, 14)

    cards = [Card(v, s) for s in suits for v in values]
    shoe = cards * num_decks
    random.shuffle(shoe)

    return shoe


def initialize_table(num_players: int=1) -> Table:
    players = [Player(id=id) for id in range(num_players)]
    table = Table(players=players)

    return table


def deal_player_cards(table: Table, shoe: Shoe, player: Player=None) -> None:
    if not player:
        players = table.players
    else:
        players = [player]

    for player in players:
        player.cards.append(shoe.pop())

    return


def deal_dealer_cards(table: Table, shoe: Shoe) -> None:
    table.dealer_cards.append(shoe.pop())

    return
