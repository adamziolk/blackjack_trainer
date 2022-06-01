if __package__ is None or __package__ == '':
    # uses current directory visibility
    import custom_types
else:
    # uses current package visibility
    import blackjack.custom_types as custom_types



def check_bust(player):
    if not check_aces(player):
        if sum([c.true_value for c in player.cards]) > 21:
            return True
        else:
            return False
    else: # They have an ace
        pass