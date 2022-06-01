import random

import blackjack.setup as setup
import blackjack.custom_types as custom_types
import blackjack.io_functions as io_functions


def play_backjack(players, num_decks=1):
    print("Here we go!")
    # random.seed(0)
    random.seed(3)
    shoe = setup.make_shoe(num_decks)
    table = setup.initialize_table(players)
    setup.deal_player_cards(shoe, players=[p0, p1, p2])
    setup.deal_dealer_cards(table, shoe)

    # print('1', '\n', table)
    # setup.deal_player_cards(shoe, players=[p0, p1, p2])
    # setup.deal_dealer_cards(table, shoe)
    # print('2', '\n', table)
    # players[0].hit(shoe)
    # print('3', '\n', table)
    # players[2].hit(shoe)
    # print('4', '\n', table)
    # players[1].split()
    # print('5', '\n', table)
    # players[1].hit(shoe)
    # players[1].split_hit(shoe)
    # print('6', '\n', table)
    # print('7', '\n')

    setup.deal_player_cards(shoe, players=[p0, p1, p2])
    setup.deal_dealer_cards(table, shoe)
    players[0].hit(shoe)
    players[1].split()
    players[1].hit(shoe)
    players[1].split_hit(shoe)
    players[2].hit(shoe)
    io_functions.display_table(table)



p0 = custom_types.Player(0)
p1 = custom_types.Player(1)
p2 = custom_types.Player(2)


play_backjack(players=[p0, p1, p2])

