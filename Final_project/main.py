from generating_cards import creating_deck
from dealing_cards_to_players import deal_cards_to_players, get_unique_usernames
from deciding_trump_suit import players_first_three_cards, decide_trump_suit
from bid_saying import saying_bid, player_bids_to_list
from gameplay import Game
from scores_calculating import calculating_scores, checking_bonus, scores_to_list
from deciding_winner import winner
from draw_table import draw_table

def main():
    player_names = get_unique_usernames()
    players_scores = {name: [] for name in player_names}
    players_bonus = {name: [] for name in player_names}
    temp_player_names = player_names

    for _ in range(4):
        card_deck = creating_deck()
        player_cards = deal_cards_to_players(card_deck, player_names)
        player = player_names[0]
        first_three_cards = players_first_three_cards(player, player_cards)
        trump_suit = decide_trump_suit(player, first_three_cards)
        players_bids = saying_bid(player_names, player_cards)
        players_bids_list = player_bids_to_list(players_bids, temp_player_names)
        game = Game(player_names, player_cards, trump_suit)
        players_won_tricks = game.game()
        players_scores, players_bonus = calculating_scores(player_names, players_bids, players_won_tricks, players_scores, players_bonus)
        players_scores_list = scores_to_list(players_scores, temp_player_names)
        draw_table(temp_player_names, players_bids_list, players_scores_list)
        print(players_bids)
        print(players_scores)
        player_names.remove(player)
        player_names.append(player)
    final_scores = checking_bonus(player_names, players_bonus, players_scores)
    winner_player = winner(player_names, final_scores)
    print(winner_player)


if __name__ == "__main__":
    main()