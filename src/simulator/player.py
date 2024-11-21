# Container class for Player information and Player Logic
import random

class Player():
    def __init__(self):
        self.is_dead = False
        self.shots_remaining = 6
        self.death_num = random.randint(1, 6)
        self.game_state = []
        self.hand = []

    def play_card(self):
        return

    def play_dice(self):
        return
