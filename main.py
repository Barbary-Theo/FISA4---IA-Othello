
from game import Game
from player import Player


def launch_analytics_mode():
    types = [Player.POSITIONAL,  Player.ABSOLUTE, Player.MOBILITY, Player.MIXT]
    profondeurs = [1, 2, 3, 4]

    for profondeur in profondeurs:
        for type1 in types:
            for type2 in types:

                p1 = Player("Théo", "white", [
                    {"x": 3, "y": 3},
                    {"x": 4, "y": 4},
                ], Player.AI, Player.WHITE, type1)
                p2 = Player("Martin", "Black", [
                    {"x": 3, "y": 4},
                    {"x": 4, "y": 3},
                ], Player.AI, Player.BLACK, type2)

                game = Game(p1, p2, 8, 8, profondeur)
                game.start_game()

                with open(f"result{profondeur}.csv", "a") as f:
                    f.write("Joueur;Joueur1;Joueur2;\n")
                    f.write(f"Type;{type1};{type2};\n")
                    f.write(f"Points;{len(game.p1.pawn_set)};{len(game.p2.pawn_set)};\n")
                    f.write(f"Gagnant;{1 if len(game.p1.pawn_set)>len(game.p2.pawn_set) else 0};{0 if len(game.p1.pawn_set)>len(game.p2.pawn_set) else 1};\n\n")

            with open(f"result{profondeur}.csv", "a") as f:
                f.write("------;\n\n")


def launch_iteration_mode():
    types = [Player.POSITIONAL,  Player.ABSOLUTE, Player.MOBILITY, Player.MIXT]
    profondeurs = [1, 2, 3, 4]

    for profondeur in profondeurs:
        for type_to_do in types:

            p1 = Player("Théo", "white", [
                {"x": 3, "y": 3},
                {"x": 4, "y": 4},
            ], Player.AI, Player.WHITE, type_to_do)
            p2 = Player("Martin", "Black", [
                {"x": 3, "y": 4},
                {"x": 4, "y": 3},
            ], Player.AI, Player.BLACK, type_to_do)

            game = Game(p1, p2, 8, 8, profondeur)
            game.start_game()


def launch_normal_game():
    p1 = Player("Théo", "white", [
        {"x": 3, "y": 3},
        {"x": 4, "y": 4},
    ], Player.AI, Player.WHITE, Player.ABSOLUTE)
    p2 = Player("Martin", "Black", [
        {"x": 3, "y": 4},
        {"x": 4, "y": 3},
    ], Player.AI, Player.BLACK, Player.ABSOLUTE)

    game = Game(p1, p2, 8, 8, 1)
    game.start_game()


def prog():
    launch_normal_game()


if __name__ == "__main__":
    prog()
