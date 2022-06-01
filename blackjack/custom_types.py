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
        self.true_value = 10 if value in (11, 12, 13) else value

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
    def __init__(self, id, chips=100):
        self.id = id
        self.cards = []
        self.split_cards = None
        self.chips = chips
        self.bet = 0

    def make_bet(self, bet_size=1):
        if bet_size > self.chips:
            raise ValueError("Insufficient funds")
        self.bet = bet_size
        self.chips -= bet_size

    def hit(self, shoe):
        setup.deal_player_cards(shoe=shoe, players=[self])

    def _check_split(self):
        return (self.cards[0].true_value == self.cards[1].true_value) and (self.chips >= self.bet)

    def split(self):
        if self._check_split():
            self.split_cards = []
            self.split_cards.append(self.cards.pop())
            self.bet += self.bet
            self.chips -= self.bet
        else:
            raise ValueError("Cards must be of the same value to split | insufficient funds")

    def split_hit(self, shoe):
        setup.deal_player_cards(shoe=shoe, players=[self], split_deal=True)

    def _check_double_down(self):
        return (self.chips >= self.bet) and (len(self.cards) <= 3) and (sum([c.true_value for c in self.cards]) in (10, 11))

    def double_down(self):
        if self._check_double_down():
            self.bet += self.bet
            self.chips -= self.chips
        else:
            raise ValueError("Cannot double down")

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
