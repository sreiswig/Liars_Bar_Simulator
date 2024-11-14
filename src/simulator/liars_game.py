# There are 4 players at the beginning of the game
# Each player is dealt 5 cards from a Deck of 6 Kings, 6 Queens, 6 Jacks, 6 Aces and 2 Jokers
# A Table value is chosen from the set (King, Queen, Jack, Ace)
# A player is chosen to go first
# The player then picks between 1 - 3 cards to place on the table
# The turn is passed to the next player (index + 1) % 4
# The current player gets to accuse or play
# If the player chooses to accuse then the last cards played are revealed
# If the revealed cards are all the same as the table value then the current player rolls to see if they die
# Else the accused player rolls to see if they die
# Special Conditions:
# If a player has played all their cards they are skipped
# If all cards have been played the last player must accuse the previous player

from player import Player
import random


class Card():
    def __init__(self, face):
        self.face = face


class LiarsGameDeck():
    def __init__(self):
        self.deck = []
        for i in range(6):
            self.deck.append(Card("King"))
            self.deck.append(Card("Queen"))
            self.deck.append(Card("Jack"))
            self.deck.append(Card("Ace"))
            if i < 2:
                self.deck.append(Card("Joker"))

    def deal(self, num_players):
        return random.sample(self.deck, num_players * 5)


class LiarsGame():
    """
    There are 4 players at the beginning of the game.
    A face is chosen to be the table_face which are the face cards that are safe to play.
    Faces are from the set of (King, Queen, Jack, Ace)
    A player is chosen to start the round.
    """
    def __init__(self, players):
        self.deck = LiarsGameDeck()
        self.players = players
        self.current_player = None
        self.table_face = None
        self.create_new_round()
    
    """
    Creates a new round.
    New Deal is made.
    """
    def create_new_round(self):
        random_draw = self.deck.deal(len(self.players))
        for i in range(4):
            self.players[i] = random_draw[(i*5) : (i*5)+5]
        self.current_player = random.sample(self.players, 1)

    """
    Turn during each turn a player plays their cards or accuses the previous player

    """
    def play(self):
        return
