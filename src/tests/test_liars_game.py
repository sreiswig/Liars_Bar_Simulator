from simulator import LiarsGame
from simulator import Player

def test_initialize_game():
    players = [Player(), Player(), Player(), Player()]
    game = LiarsGame(players)
    assert len(game.players) == 4
