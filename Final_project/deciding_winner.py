def winner(players, final_scores):
    """
    this function is returning the winner of the game
    """
    max_score = sum(final_scores[players[0]])
    winner = ""
    winners = []
    for player in players:
        if sum(final_scores[player]) >= max_score:
            if sum(final_scores[player]) == max_score:
                winners.append(winner)
                winners.append(player)
            else:
                max_score = sum(final_scores[player])
                winner = player
                winners.clear()
    if len(winners) > 1:
        return f"{', '.join(winners)} are tied with {max_score} points"
    return f"{winner} is the winner of the game with {max_score} points"