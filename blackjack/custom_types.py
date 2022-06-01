if __package__ is None or __package__ == '':
    # uses current directory visibility
    import setup
else:
    # uses current package visibility
    import blackjack.setup as setup

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{self.suit}'

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value and self.suit == other.suit
        return False

    def __hash__(self):
        return hash(f'{self.value} {self.suit}')


class Shoe:
    pass
    # Shoe = list[Card]


class Player:
    def __init__(self, id):
        self.id = id
        self.cards = []
        self.split_cards = None

    def hit(self, shoe):
        setup.deal_player_cards(shoe=shoe, players=[self])

    def split(self):
        self.split_cards = []
        self.split_cards.append(self.cards.pop())

    def split_hit(self, shoe):
        setup.deal_player_cards(shoe=shoe, players=[self], split_deal=True)

    def __repr__(self):
        if self.split_cards:
            return f'{self.id} - {self.cards} - split: {self.split_cards}'
        return f'{self.id} - {self.cards}'

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.cards == other.cards
        return False

    def __hash__(self):
        return hash(f'{self.id} {self.cards}')


class Table:
    def __init__(self, players):
        self.dealer_cards = []
        self.players = players

    def __repr__(self):
        return f'DC: {self.dealer_cards} :: {[f"{p}" for p in self.players]}'

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.dealer_cards == other.dealer_cards and self.players == other.players
        return False

    def __hash__(self):
        return hash(f'{self.dealer_cards} {self.players}')
