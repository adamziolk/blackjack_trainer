class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Shoe:
    pass
    # Shoe = list[Card]


class Player:
    def __init__(self, id):
        self.id = id
        self.cards = []


class Table:
    def __init__(self, players):
        self.dealer_cards = []
        self.players = players
