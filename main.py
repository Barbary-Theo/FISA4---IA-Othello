
from map import Map
from player import Player


def prog():

    map = Map()
    map.print()

    p1 = Player("Théo", "white", [1, 2, 3])
    p2 = Player("Martin", "Black")



if __name__ == "__main__":
    prog()
