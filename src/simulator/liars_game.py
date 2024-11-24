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
        self.players = players
        self.previous_player = None
        self.current_player = None
        self.table_face = None
        self.last_played = []
        self.game_state = None
        self.face_set = ("King", "Queen", "Jack", "Ace")
    
    """
    A table value is chosen from the faces (King, Queen, Jack, Ace)
    Players must play 1 - 3 cards of the face value or play other face cards and lie
    The next player either plays their 1 - 3 cards or accuses the previous player
    If a player doesn't have cards they are skipped
    A round ends when an accusation is made or all cards are played and the last player is forced to accuse
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
    A game ends when only one player is left alive
    """
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
