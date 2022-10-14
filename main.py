
from game import Game
from player import Player


def prog():

    p1 = Player("Théo", "white", [
        {"x": 0, "y": 0}, {"x": 1, "y": 0},
        {"x": 2, "y": 0}, {"x": 3, "y": 0},
        {"x": 4, "y": 0}, {"x": 5, "y": 0},
        {"x": 6, "y": 0}, {"x": 7, "y": 0},
    ])
    p2 = Player("Martin", "Black", [
        {"x": 0, "y": 7}, {"x": 1, "y": 7},
        {"x": 2, "y": 7}, {"x": 3, "y": 7},
        {"x": 4, "y": 7}, {"x": 5, "y": 7},
        {"x": 6, "y": 7}, {"x": 7, "y": 7},
    ])

    game = Game(p1, p2, 8, 8)
    #game.print_all()
    game.print()



if __name__ == "__main__":
    prog()
