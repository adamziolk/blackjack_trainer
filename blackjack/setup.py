import random
from typing import Optional, Any


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


def deal_cards(table: Table, shoe: Shoe, players: Optional[list[int]]=None) -> None:
    if not players:
        players = [p.id for p in table.players]

    for player in players:
        table[player].append(shoe.pop())

    return
