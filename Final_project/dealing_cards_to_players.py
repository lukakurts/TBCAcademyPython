PLAYERS_NUMBER = 4
from random import shuffle, sample, choice
"""
this function reads players names randomly choses last player names 
than randomly shuffles other players and return all player names
"""
def get_unique_usernames():
    players = set()
    while len(players) < PLAYERS_NUMBER:
        username = input(f"Enter player {len(players) + 1} name: ")

        if username in players:
            print("Username already exists. Choose another.")
        elif username == "":
            print("Username can't be empty.")
        else:
            players.add(username)
    players = list(players)
    last_player = choice(players)
    players.remove(last_player)
    shuffle(players)
    players.append(last_player)
    
    return players

def deal_cards_to_players(all_cards, players):
    """
    this function is randomly dealing cards to all players
    returns dictionary, keys are player names and values are players cards
    """
    player_cards = {}

    for player in players:
        player_cards[player] = sample(all_cards, 9)
        for card in player_cards[player]:
            all_cards.remove(card)

    return player_cards 