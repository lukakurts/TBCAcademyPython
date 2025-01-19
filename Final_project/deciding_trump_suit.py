from time import sleep

def players_first_three_cards(player, players_card):
    """
    this function is returning list of first three cards of selected player
    """
    first_three_card = []
    for i in range(3):
        card = players_card[player][i]
        first_three_card.append(card)

    return first_three_card

def decide_trump_suit(player, first_three_card):
    """
    this function returns the trump suit
    """
    # sleep(5)
    print(first_three_card)
    print(f"{player} please decide trump suit.")
    player_input = input("Plese enter 'h', 'c', 's', 'd' or press enter for non of them: ").lower()
    match player_input:
        case "h":
            return '♥'
        case "c":
            return '♣'
        case "s":
            return '♠'
        case "d":
            return '♦'
        case "":
            return None
        case _:
            print("wrong input")
            return decide_trump_suit(player, first_three_card)