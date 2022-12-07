from rich import console

import game
import player


class Player:
    console = console.Console()
    REAL = "real"
    AI = "ai"

    def __init__(self, name: str = None,
                 couleur: str = "white",
                 pawn_set: list = None,
                 type: str = "real",
                 symbol: str = "o"):

        if pawn_set is None:
            pawn_set = []
        self.name = name
        self.couleur = couleur
        self.pawn_set = pawn_set
        self.type = type
        self.symbol = symbol

    def print(self):
        set_creation = ""
        for object in self.pawn_set:
            set_creation += "\n    {x: \"" + str(object.get("x")) + "\", y: \"" + str(object.get("y")) + "\"}"

        self.console.print(
            "player { \n  name: \"" + self.name + "\",\n  couleur: \"" + self.couleur + "\"\n  pawn: [" + set_creation + "\n  ]\n}")

    def exist_enemy_pawn_arround(self, map: list, position: dict):

        positions_arround = [(-1, -1), (0, -1), (1, -1),
                             (-1, 0), (1, 0),
                             (-1, 1), (0, 1), (1, 1)]

        for position_arround in positions_arround:
            try:
                value = map[position.get("y") + position_arround[1]][position.get("x") + position_arround[0]]
                if value != "." and value != self.symbol:
                    return True
            except Exception:
                pass

        return False


    def do_the_play(self, x, y, map):
        if x < 0 or y < 0:
            self.console.print("Please check your inputs\n", style="red")
        elif self.exist_enemy_pawn_arround(map, {"x": x, "y": y}):
            if map[y][x] == ".":
                self.pawn_set.append({"x": x, "y": y})
                return {"x": x, "y": y}
            else:
                self.console.print("❌ Position already token ❌", style="red")
                self.console.print()
        elif self.type == Player.REAL:
            self.console.print("❌ No pawn arround this position ❌", style="red")
            self.console.print()

        return None


    def play(self, map):

        is_a_good_placement = False

        while not is_a_good_placement:

            self.console.print("\nChoose a position to put your pawn", style="yellow")

            try:
                self.console.print("-> Column number : ", style="yellow", end="")
                x = int(input())
                self.console.print("-> Row number : ", style="yellow", end="")
                y = int(input())

                play = self.do_the_play(x, y, map)

                if play is not None:
                    return play

            except Exception:
                self.console.print("Please check your inputs\n", style="red")


    def is_a_possible_play(self, map, x, y, index_x, index_y, possible_plays):
        return map[y - index_y][x - index_x] == "." and {"y": y - index_y, "x": x - index_x} not in possible_plays


    def get_posible_position(self, map, enemy_player):

        possible_plays = []

        for enemy_position in enemy_player.pawn_set:

            y = enemy_position["y"]
            x = enemy_position["x"]

            index_x = [-1, 0, 1]
            index_y = [-1, 0, 1]

            for x_val in index_x:
                for y_val in index_y:

                    try:
                        if self.is_a_possible_play(map, x, y, x_val, y_val, possible_plays):
                            possible_plays.append({"y": y - y_val, "x": x - x_val})
                    except Exception:
                        pass

        return possible_plays


    def get_best_play(self,map, enemy_player, depth_still_to_do, moves):

        if depth_still_to_do == 0:
            return moves

        print("depth ", depth_still_to_do)

        possible_plays = self.get_posible_position(map, enemy_player)
        possible_plays_result = possible_plays

        for play_index in range(len(possible_plays)):
            play = possible_plays[play_index]
            print(play)
            moves.append(play)
            game_simulate = game.Game(self, enemy_player, 8, 8, depth_still_to_do)
            self.do_the_play(play["x"], play["y"], map)
            possible_plays_result[play_index]["move"] = self.get_best_play(game_simulate.map, enemy_player, depth_still_to_do - 1, moves)

        return possible_plays_result

    def ia_play(self, map, enemy_player, total_depth=2):

        """
        TODO
            -> implement IA method to play
        """

        moves = self.get_best_play(map, enemy_player, total_depth - 1, [])
        print(moves)

        return {"x": -1, "y": -1}




