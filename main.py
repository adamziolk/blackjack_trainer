import random

import blackjack.setup as setup

def play_backjack(num_players=1, num_decks=1):
    print("Here we go!")
    # random.seed(0)
    shoe = setup.make_shoe(num_decks)
    table = setup.initialize_table(num_players)
    setup.deal_cards(table, shoe)
    setup.deal_cards(table, shoe)

    print(table)

play_backjack()

