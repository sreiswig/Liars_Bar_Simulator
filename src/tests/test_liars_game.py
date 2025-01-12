from simulator import LiarsGame
from simulator import Player
from simulator.liars_game import LiarsGameDeck

def test_deck():
    deck = LiarsGameDeck()
    face_counts = {"King": 0, "Queen": 0, "Jack": 0, "Ace": 0, "Joker": 0}
    for card in deck.deck:
        face_counts[card.face] = face_counts[card.face] + 1

    assert face_counts["King"] == 6
    assert face_counts["Queen"] == 6
    assert face_counts["Jack"] == 6
    assert face_counts["Ace"] == 6
    assert face_counts["Joker"] == 2

def test_game_setup():
    return
