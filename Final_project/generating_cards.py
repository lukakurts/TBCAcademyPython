from random import shuffle

def creating_deck():
    """
    this function is creating deck and adding jokers instead of 6♣ and 6♠
    return list of all cards
    """
    suits = ['♣', '♦', '♥', '♠']
    values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6']
    all_cards = []
    for suit in suits:
        for value in values:
            card = f"{value}{suit}"
            if card == "6♣" or card == "6♠":
                card = "Joker"
            all_cards.append(card)
    shuffle(all_cards)

    return all_cards