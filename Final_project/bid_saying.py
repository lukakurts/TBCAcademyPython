from time import sleep
from clearing_terminal import clear

def players_bid(player, player_cards):
    """
    this function is taking input from players and returning the bid
    """
    print(player_cards[player])
    try:
        bid = int(input(f"{player} please say a bid: "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 9.")
        return players_bid(player, player_cards)
    if bid > 9 or bid < 0:
        print("Please say a bid between 0 and 9")
        return players_bid(player, player_cards)
    return bid


def last_player_bid(player, player_cards, bid_sum):
    """
    this function is taking input from last player and returning the bid, checking if the bid is valid or not
    """
    if 9 - bid_sum >= 0:
        print(f"You can't say {9 - bid_sum} as bid")
    else:
        print(f"You can say anything.")
    bid = players_bid(player, player_cards)
    if (9 - bid_sum) == bid:
        print("Please say a bid again")
        return last_player_bid(player, player_cards, bid_sum)
    return bid


def saying_bid(player_names, player_cards):
    """
    this function is taking bids from all players and returning the bids of all players
    return dictionary, keys are player names and values are list of bids
    """
    player_bids = {name: [] for name in player_names}
    bid_sum = 0
    for i in range(len(player_names)):
        player = player_names[i]
        clear()
        # sleep(1)
        if i == 3:
            bid = last_player_bid(player, player_cards, bid_sum)
        else:
            bid = players_bid(player, player_cards)
            bid_sum += bid
        player_bids[player].append(bid)
    return player_bids


def player_bids_to_list(player_bids, temp_players):
    """
    this function is converting the dictionary to list
    """
    player_bids_list = []
    for player in temp_players:
        player_bids_list.append(player_bids[player][0])
    return player_bids_list