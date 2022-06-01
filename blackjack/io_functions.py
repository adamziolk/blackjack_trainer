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
    print()

def prompt_user(player, shoe):
    options = ['Hit', 'Stand']
    if player._check_split():
        options.append('Split')
    if player._check_double_down():
        options.append('Double Down')

    options = {i:o for i, o in enumerate(options)}
    print(options)
    print()

    choice = input(f"Player {player.id} - What do? ")
    try:
        choice = int(choice)
    except:
        raise ValueError("Invalid Choice")

    selection = options.get(choice)
    if selection == "Hit":
        player.hit(shoe)
    elif selection == "Stand":
        pass
    elif selection == "Split":
        player.split()
        player.hit(shoe)
        player.split_hit(shoe)
    elif selection == "Double Down":
        player.double_down(shoe)
    else:
        raise ValueError("Invalid Choice")