from time import sleep
from clearing_terminal import clear

class Game:
    def __init__(self, players, player_cards, trump_suit):
        self.players = players
        self.player_cards = player_cards
        self.numerated_cards = {}
        self.trump_suit = trump_suit
        self.temp_players = players.copy()
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, players):
        self._players = players
    
    @property
    def player_cards(self):
        return self._player_cards
    
    @player_cards.setter
    def player_cards(self, player_cards):
        self._player_cards = player_cards

    @property
    def numerated_cards(self):
        return self._numerated_cards
    
    @numerated_cards.setter
    def numerated_cards(self, numerated_cards):
        self._numerated_cards = numerated_cards

    @property
    def trump_suit(self):
        return self._trump_suit
    
    @trump_suit.setter
    def trump_suit(self, trump_suit):
        self._trump_suit = trump_suit
    
    def numerate_cards(self):
        """
        this method is numerating cards
        returns dictionary, keys are player names and values are numerated cards
        """
        for player in self.temp_players:
            self._numerated_cards[player] = {i + 1: card for i, card in enumerate(self.player_cards[player])}
        return self._numerated_cards
    
    
    def player_input(self, player):
        """
        this method is taking input from players and returning the number between 1 and number of cards
        """
        len_cards = len(self._player_cards[player])
        try:
            player_choice = int(input(f"{player} please select a card: "))
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {len_cards}.")
            return self.player_input(player)
        return player_choice
    

    def picking_card(self, player):
        """
        this method is taking input from players and returning the card that player selected
        """
        player_choice = self.player_input(player)
        try:
            gone_card = self._numerated_cards[player][player_choice]
        except KeyError:
            print(f"Invalid input. Please enter a number between 1 and {len(self._player_cards[player])}.")
            return self.picking_card(player)
        return gone_card
    

    def same_suit_check(self):
        """
        this method is collecting the suits of the players
        returns dictionary, keys are player names and values are list of suits that players have
        """
        suits = {name: [] for name in self.temp_players}
        for player in self.temp_players:
            for card in self._player_cards[player]:
                suits[player].append(card[-1])
        return suits
    

    def suit_check(self, player, first_player_card, suits):
        """
        this method is checking if the player has the same suit card with the first player
        returns the card that player selected
        """
        first_player_card_suit = first_player_card[-1]
        print(self._numerated_cards[player])
        gone_card = self.picking_card(player)
        gone_card_suit = gone_card[-1]
        if first_player_card == "Joker":
            self._player_cards[player].remove(gone_card)
            suits[player].remove(gone_card_suit)
            return gone_card
        if gone_card == "Joker":
            self._player_cards[player].remove(gone_card)
            suits[player].remove(gone_card_suit)
            return gone_card
        if first_player_card_suit in suits[player] or self._trump_suit in suits[player]:
            if gone_card_suit != first_player_card_suit and gone_card_suit != self._trump_suit:
                if self.trump_suit != None:
                    print(f"{player} you should play {first_player_card_suit} or {self._trump_suit}")
                else:
                    print(f"{player} you should play {first_player_card_suit}")
                return self.suit_check(player, first_player_card, suits)
            else:
                self._player_cards[player].remove(gone_card)
                suits[player].remove(gone_card_suit)
                return gone_card
        self._player_cards[player].remove(gone_card)
        suits[player].remove(gone_card_suit)
        return gone_card

    
    def players_selected_cards(self):
        """
        this method is getting cards from players and returning the cards that players selected
        returns dictionary, keys are player names and values are list of cards that players selected
        """
        gone_cards = {name: [] for name in self.temp_players}
        self.numerate_cards()
        first_player = self.temp_players[0]
        clear()
        print(self._numerated_cards[first_player])
        first_player_card = self.picking_card(first_player)
        suits = self.same_suit_check()
        for player in self.temp_players:
            if player == first_player:
                gone_card = first_player_card
                gone_cards[player].append(gone_card)
                self._player_cards[player].remove(gone_card)
            else:
                clear()
                print(gone_cards)
                gone_card = self.suit_check(player, first_player_card, suits)
                gone_cards[player].append(gone_card)
        print(gone_cards)
        return gone_cards
    

    def game(self):
        """
        this method is getting gone cards from players and should 
        returns dictionary, keys are player names and values are list of 1s that players won
        """
        card_values = {"6": 6, "7": 7, "8": 8, "9": 9, "1": 10,
                        "J": 11, "Q": 12, "K": 13, "A": 14}
        won_tricks = {name: [] for name in self._players}
        for _ in range(9):
            first_player = self.temp_players[0]
            gone_cards = self.players_selected_cards()
            first_players_suit = gone_cards[first_player][0][-1]
            winner_player = first_player
            joker_played = False
            for player in self.temp_players:
                player_card = gone_cards[player][0]
                player_suit = player_card[-1]
                """
                this part is checking which player won the trick
                """
                if player_card == "Joker":
                    winner_player = player
                    joker_played = True
                elif player_suit == first_players_suit and (not joker_played):
                    if card_values[player_card[0]] > card_values[gone_cards[winner_player][0][0]]:
                        winner_player = player
                elif player_suit == self._trump_suit and (not joker_played):
                    winner_player = player
                    first_players_suit = self._trump_suit
            print(f"This trick's winner is {winner_player} with {gone_cards[winner_player][0]}")
            sleep(5)
            won_tricks[winner_player].append(1)
            """
            this part makes winner player first player
            """
            for _ in range(len(self.temp_players)):
                player = self.temp_players[0]
                if winner_player == player:
                    break
                else:
                    self.temp_players.remove(player)
                    self.temp_players.append(player)
        return won_tricks