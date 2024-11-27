import random

"""
Simple card with a face value
"""
class Card():
    def __init__(self, face):
        self.face = face

"""
Liars game deck made of 6 King, Queen, Jack, Ace and 2 Jokers
"""
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
        self.num_live_players = 4
        self.players = players
        self.previous_player = None
        self.current_player = random.sample([0,1,2,3], 1)
        self.table_face = None
        self.last_played = []
        self.game_state = None
        self.face_set = ("King", "Queen", "Jack", "Ace")
   
    def get_game_state(self):
        game_state = {}
        return game_state

    """
    A table value is chosen from the faces (King, Queen, Jack, Ace)
    Cards are dealt to the players
    """
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

    """
    Returns true if all cards are the table face value or Joker, false otherwise 
    """
    def accuse(self):
        return all(card.face == self.table_face for card in self.last_played)

    """
    Run a game of liars game
    A game is made of multiple rounds
    A game ends when only one player is left alive
    """
    def run(self):
        while self.num_live_players > 1:
            self.create_new_round()
            self.run_round()

    """
    The first player plays 1 - 3 cards
    The next player may play cards or accuse
    A round ends on an accusation or when all players run out of cards then the last player is forced to make an accusation
    """
    def run_round(self):
        return 
