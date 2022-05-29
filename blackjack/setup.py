import random
from typing import Any, Optional

Card = tuple[int, str]
Shoe = list[Card]
Hand = list[Card]
Table = dict[Any, Hand]

def make_shoe(num_decks: int=1) -> Shoe:
    suits = ['C', 'H', 'S', 'D']
    values = range(1, 14)

    cards = [(v, s) for s in suits for v in values]
    shoe = cards * num_decks
    random.shuffle(shoe)

    return shoe


def initialize_table(num_players: int=1) -> Table:
    table = {}
    for player in range(num_players):
        table[player] = []
    table['dealer'] = []

    return table


def deal_cards(table: Table, shoe: Shoe, players: Optional[list[int]]=None) -> None:
    if not players:
        players = table.keys()

    for player in players:
        table[player].append(shoe.pop())

    return
