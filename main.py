
from map import Map
from player import Player


def prog():

    map = Map()
    print(map)

    p1 = Player("Théo", "white", [1, 2, 3])
    p2 = Player("Martin", "Black")

    print(p1)
    print(p2)


if __name__ == "__main__":
    prog()
