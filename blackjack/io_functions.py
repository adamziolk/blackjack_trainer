if __package__ is None or __package__ == '':
    # uses current directory visibility
    import custom_types
else:
    # uses current package visibility
    import blackjack.custom_types as custom_types

def display_table(table):
    print("Dealer: ", table.dealer_cards[0], ", XX")
    
    for i, p in enumerate(table.players):
        if p.split_cards:
            print(f"Player {i}: ", f"{p.cards} - split: {p.split_cards}")
        else:
            print(f"Player {i}: ", f"{p.cards}")