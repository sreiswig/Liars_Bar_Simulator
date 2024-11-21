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
        self.previous_player = None
        self.current_player = None
        self.table_face = None
        self.last_played = []
        self.game_state = None
        self.face_set = ("King", "Queen", "Jack", "Ace")
    

    def create_new_round(self):
        random_draw = self.deck.deal(len(self.players))
        for i in range(4):
            self.players[i] = random_draw[(i*5) : (i*5)+5]
        self.current_player = random.sample([0,1,2,3], 1)
        self.table_face = random.sample(self.face_set, 1)

    def take_shot(self, player):
        if random.randint(1, player.shots_remaining) == player.death_num:
            player.is_dead = True
        else:
            player.shots_remaining = player.shots_remaining - 1

    def accuse(self):
        return all(card.face == self.table_face for card in self.last_played)

    def run(self):
        self.create_new_round()
        match self.players[self.current_player].play_cards(self.game_state):
            case ("Accuse", []):
                if self.accuse():
                    self.take_shot(self.current_player)
                else:
                    self.take_shot(self.previous_player)
            case ("Play", _):
                return
            case _:
                return
