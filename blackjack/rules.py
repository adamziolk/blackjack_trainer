if __package__ is None or __package__ == '':
    # uses current directory visibility
    import custom_types
else:
    # uses current package visibility
    import blackjack.custom_types as custom_types



def check_bust(player):
    if player.hand_total() > 21:
        return True
    return False