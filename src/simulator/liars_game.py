# There are 4 players at the beginning of the game
# Each player is dealt 5 cards from a Deck of 6 Kings, 6 Queens, 6 Jacks, 6 Aces and 2 Jokers
# A Table value is chosen from the set (King, Queen, Jack, Ace)
# A player is chosen to go first
# The player then pick between 1 - 3 cards to place on the table
# The turn is passed to the next player (index + 1) % 4
# The current player gets to accuse or play
# If the player chooses to accuse then the last cards played are revealed
# If the revealed cards are all the same as the table value then the current player rolls to see if they die
# Else the accused player rolls to see if they die
# Special Conditions:
# If a player has played all their cards they are skipped
# If all cards have been played the last player must accuse the previous player
from player import Player

class Card():
    def __init__(self, face):
        self.face = face

class LiarsGameDeck():
    def __init__(self):
        return

    def draw(self, num):
        return

class LiarsGame():
    def __init__(self, players):
        self.deck = None
        self.last_played = []
        self.current_player = None
        self.players = players

    def deal(self):
        return
