import random

import blackjack.setup as setup
import blackjack.custom_types as custom_types

def play_backjack(players, num_decks=1):
    print("Here we go!")
    random.seed(0)
    shoe = setup.make_shoe(num_decks)
    table = setup.initialize_table(players)
    setup.deal_player_cards(table, shoe)
    setup.deal_dealer_cards(table, shoe)
    print('1', '\n', table)
    setup.deal_player_cards(table, shoe)
    setup.deal_dealer_cards(table, shoe)
    print('2', '\n', table)
    players[0].hit(table, shoe)
    print('3', '\n', table)
    players[2].hit(table, shoe)
    print('4', '\n', table)

p0 = custom_types.Player(0)
p1 = custom_types.Player(1)
p2 = custom_types.Player(2)


play_backjack(players=[p0, p1, p2])

