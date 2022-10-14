
from game import Game
from player import Player


def prog():

    p1 = Player("Théo", "white", [
        {"x": 3, "y": 3},
        {"x": 4, "y": 4},
    ])
    p2 = Player("Martin", "Black", [
        {"x": 3, "y": 4},
        {"x": 4, "y": 3},
    ])

    game = Game(p1, p2, 8, 8)
    game.start_game()



if __name__ == "__main__":
    prog()
