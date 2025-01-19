def calculating_scores(players, players_bids, players_won_tricks, players_scores, players_bonus):
    """
    this function is calculating the scores of the players
    returns dictionary, keys are player names and values are list of scores of the players
    """
    for player in players:
        if sum(players_bids[player]) == sum(players_won_tricks[player]):
            if sum(players_bids[player]) == 9:
                players_scores[player].append(900)
            players_scores[player].append(50 + 50 * sum(players_bids[player]))
            players_bonus[player].append(1)
        elif sum(players_won_tricks[player]) == 0:
            players_scores[player].append(-500)
        else:
            players_scores[player].append(10 * sum(players_won_tricks[player]))
    return players_scores, players_bonus


def scores_to_list(players_scores, temp_players):
    player_scores_list = []
    for player in temp_players:
        player_scores_list.append(players_scores[player][-1])
    return player_scores_list
            
            
def checking_bonus(players, players_bonus, players_scores):
    """
    this function is checking if player should have bonus score
    returns dictionary, keys are player names and values are list of scores of the players with bonus
    """
    for player in players:
        if sum(players_bonus[player]) == 4:
            max_score = max(players_scores[player])
            players_scores[player].append(max_score)
    return players_scores