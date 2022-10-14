
from game import Game
from player import Player


def prog():

    p1 = Player("Théo", "white", [1, 2, 3])
    p2 = Player("Martin", "Black")

    game = Game(p1, p2, 8, 8)
    game.print()



if __name__ == "__main__":
    prog()
