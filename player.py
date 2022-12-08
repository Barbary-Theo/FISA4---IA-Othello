import json

from rich import console

import game
import config


class Player:
    console = console.Console()

    REAL = "real"
    AI = "ai"

    WHITE = "o"
    BLACK = "x"

    POSITIONAL = "positional"
    ABSOLUTE = "absolute"
    MOBILITY = "mobility"
    MIXT = "mixt"

    def __init__(self, name: str = None,
                 couleur: str = "white",
                 pawn_set: list = None,
                 type: str = "real",
                 symbol: str = WHITE,
                 ai_type: str = POSITIONAL):

        if pawn_set is None:
            pawn_set = []
        self.name = name
        self.couleur = couleur
        self.pawn_set = pawn_set
        self.type = type
        self.symbol = symbol
        self.ai_type = ai_type


    def __copy__(self):
        return Player(self.name,
                      self.couleur,
                      self.pawn_set.copy(),
                      self.type,
                      self.symbol)

    def print(self):
        set_creation = ""
        for object in self.pawn_set:
            set_creation += "\n    {x: \"" + str(object.get("x")) + "\", y: \"" + str(object.get("y")) + "\"}"

        self.console.print(
            "player { \n  name: \"" + self.name + "\",\n  couleur: \"" + self.couleur + "\"\n  pawn: [" + set_creation + "\n  ]\n}")

    def is_a_right_position(self, map: list, position: dict, current_player):

        positions_arround = [(-1, -1), (0, -1), (1, -1),
                             (-1, 0), (1, 0),
                             (-1, 1), (0, 1), (1, 1)]

        for position_arround in positions_arround:
            try:
                value = map[position.get("y") + position_arround[1]][position.get("x") + position_arround[0]]
                is_in_game_position = 0 <= position["x"] < 8 and 0 <= position["y"] < 8
                if value != "." and value != current_player.symbol and is_in_game_position:
                    coef = 1
                    is_a_point = False
                    while not is_a_point:
                        try:
                            if coef > 10:
                                break

                            previous_value = map[position.get("y") + coef * position_arround[1]][position.get("x") + coef * position_arround[0]]
                            if previous_value == current_player.symbol:
                                return True
                            elif previous_value == ".":
                                is_a_point = True

                            coef += 1
                        except Exception:
                            is_a_point = True

            except Exception:
                pass

        return False


    def do_the_play(self, x, y, map, current_player):
        if (x < 0 or y < 0) and current_player.type == Player.REAL:
            self.console.print("Please check your inputs\n", style="red")
        elif current_player.is_a_right_position(map, {"x": x, "y": y}, current_player):

            if map[y][x] == ".":
                current_player.pawn_set.append({"x": x, "y": y})
                return {"x": x, "y": y}
            elif current_player.type == Player.REAL:
                self.console.print("❌ Position already token ❌", style="red")
                self.console.print()

        elif current_player.type == Player.REAL:
            self.console.print("❌ No pawn arround this position ❌", style="red")
            self.console.print()

        return None


    def play(self, map, enemy_player):

        possible_play = self.get_possible_position(map, self, enemy_player)
        if len(possible_play) == 0:
            return {"x": -1, "y": -1}

        is_a_good_placement = False

        while not is_a_good_placement:

            self.console.print("\nChoose a position to put your pawn", style="yellow")

            try:
                self.console.print("-> Column number : ", style="yellow", end="")
                x = int(input())
                self.console.print("-> Row number : ", style="yellow", end="")
                y = int(input())

                play = self.do_the_play(x, y, map, self)

                if play is not None:
                    return play

            except Exception:
                self.console.print("Please check your inputs\n", style="red")


    def get_possible_position(self, map, current_player, enemy_player):

        possible_plays = []

        for enemy_position in enemy_player.pawn_set:

            y = enemy_position["y"]
            x = enemy_position["x"]

            index_x = [-1, 0, 1]
            index_y = [-1, 0, 1]

            for x_val in index_x:
                for y_val in index_y:

                    try:
                        position_to_check = {"x": x - x_val, "y": y - y_val}
                        if current_player.is_a_right_position(map, position_to_check, current_player) \
                                and position_to_check not in possible_plays \
                                and map[position_to_check["y"]][position_to_check["x"]] == ".":
                            possible_plays.append(position_to_check)
                    except Exception:
                        pass

        return possible_plays


    def get_best_play(self, map, current_player, enemy_player, depth_still_to_do, total_depth):

        if depth_still_to_do < 0:
            return []

        possible_plays = current_player.get_possible_position(map, current_player, enemy_player)
        possible_plays_result = possible_plays.copy()

        if len(possible_plays) == 0:
            return []

        depth_still_to_do -= 1

        for play_index in range(len(possible_plays)):
            possible_plays_result[play_index]["depth"] = total_depth - (depth_still_to_do + 1)

            current_player_copy = current_player.__copy__()
            enemy_player_copy = enemy_player.__copy__()

            p1, p2 = (current_player_copy, enemy_player_copy) if current_player.symbol == Player.WHITE else (enemy_player_copy, current_player_copy)

            play = possible_plays[play_index]

            game_simulate = game.Game(p1, p2, 8, 8, depth_still_to_do)
            current_player_copy.do_the_play(play["x"], play["y"], game_simulate.map, p2)
            game_simulate.update_map()
            possible_plays_result[play_index]["nb_stolen"] = game_simulate.check_if_a_pawn_have_to_swap_team(current_player_copy, enemy_player_copy, {"x": play["x"], "y": play["y"]})
            game_simulate.update_map()

            possible_plays_result[play_index]["case_static_value"] = config.STATIC_VALUES_OTHELLO[play.get("x")][play.get("y")]
            possible_plays_result[play_index]["move"] = current_player_copy.get_best_play(game_simulate.map, enemy_player_copy,
                                                                           current_player_copy, depth_still_to_do, total_depth)

        return possible_plays_result


    def ia_play(self, map, enemy_player, total_depth=1):

        """
        TODO
            -> implement IA method to play
        """

        moves = self.get_best_play(map, self, enemy_player, total_depth, total_depth)

        #self.write_moves(moves)

        moves_to_do = self.select_a_move(moves)

        move_to_do = moves[0] if len(moves) > 0 else {"x": -1, "y": -1}
        self.do_the_play(move_to_do["x"], move_to_do["y"], map, self)

        return move_to_do


    def select_a_move(self, moves: list):

        if self.ai_type == Player.POSITIONAL:
            return self.move_positional(moves)
        if self.ai_type == Player.MOBILITY:
            return self.move_mobility(moves)
        if self.ai_type == Player.MIXT:
            return self.move_mixt(moves)
        if self.ai_type == Player.ABSOLUTE:
            return self.move_absolute(moves)

        return moves[0]


    def move_positional(self, moves: list):
        return moves[0]

    def move_mobility(self, moves: list):
            return moves[0]

    def move_absolute(self, moves: list):
        return moves[0]

    def move_mixte(self, moves: list):
        return moves[0]

    def write_moves(self, moves):
        with open("moves.txt", "w") as f:
            f.write(moves.__str__().replace("'", "\""))


