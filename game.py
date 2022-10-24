from rich.text import Text
from player import Player
from rich import console


class Game:
    console = console.Console()

    def __init__(self, p1: Player = None,
                 p2: Player = None,
                 nb_row=8,
                 nb_col=8):

        self.p1 = p1
        self.p2 = p2
        self.map = self.init_map(nb_row, nb_col)

    def init_map(self, nb_row, nb_col):
        map = []
        for i in range(nb_row):
            row = []
            for j in range(nb_col):
                if self.p1.pawn_set.__contains__({"x": j, "y": i}):
                    row.append("o")
                elif self.p2.pawn_set.__contains__({"x": j, "y": i}):
                    row.append("x")
                else:
                    row.append(".")
            map.append(row)

        return map

    def print(self):

        self.console.print("    ", end="")
        for i in range(len(self.map)):
            self.console.print("[red]" + str(i) + "[/]", style="underline", end="")
            self.console.print("  ", end="")

        self.console.print("")
        row_number = 0

        for row in self.map:
            string = "[red]" + str(row_number) + "|  " + "[/]"
            for col in row:
                string += str(col) + "  "
            row_number += 1
            self.console.print(string)

    def print_all(self):
        self.print()
        self.p1.print()
        self.p2.print()

    def update_map(self):
        for pawn in self.p1.pawn_set:
            self.map[pawn.get("x")][pawn.get("y")] = "o"

        for pawn in self.p2.pawn_set:
            self.map[pawn.get("x")][pawn.get("y")] = "x"

    def check_nb_to_still_to_left(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y")) - 1
        index_y = int(position_played.get("x"))
        position_to_swap = []

        while index_x >= 0 and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_x -= 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_right(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y")) + 1
        index_y = int(position_played.get("x"))
        position_to_swap = []

        while index_x < len(self.map[0]) and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_x += 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_top(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y"))
        index_y = int(position_played.get("x")) - 1
        position_to_swap = []

        while index_y >= 0 and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_y -= 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_bottom(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y"))
        index_y = int(position_played.get("x")) + 1
        position_to_swap = []

        while index_y < len(self.map) and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_y += 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_top_left(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y")) - 1
        index_y = int(position_played.get("x")) - 1
        position_to_swap = []

        while index_y >= 0 and index_x >= 0 and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_y -= 1
            index_x -= 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_top_right(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y")) + 1
        index_y = int(position_played.get("x")) - 1
        position_to_swap = []

        while index_y >= 0 and index_x < len(self.map[0]) and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_y -= 1
            index_x += 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_bottom_left(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y")) - 1
        index_y = int(position_played.get("x")) + 1
        position_to_swap = []

        while index_y < len(self.map) and index_x >= 0 and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_y += 1
            index_x -= 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def check_nb_to_still_to_bottom_right(self, position_played, player_who_played, player_to_check):
        index_x = int(position_played.get("y")) + 1
        index_y = int(position_played.get("x")) + 1
        position_to_swap = []

        while index_y < len(self.map) and index_x < len(self.map[0]) and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_y += 1
            index_x += 1

        if self.map[index_y][index_x] == player_who_played.symbol:
            for position in position_to_swap:
                player_to_check.pawn_set.remove(position)
                player_who_played.pawn_set.append(position)

        return player_to_check, player_who_played

    def swap_type_if_spawn_circled(self, player_who_played, player_to_check_pawn, position_played):
        players = self.check_nb_to_still_to_left(position_played, player_who_played, player_to_check_pawn)
        players = self.check_nb_to_still_to_right(position_played, players[0], players[1])
        players = self.check_nb_to_still_to_top(position_played, players[0], players[1])
        players = self.check_nb_to_still_to_bottom(position_played, players[0], players[1])

        players = self.check_nb_to_still_to_top_left(position_played, players[0], players[1])
        players = self.check_nb_to_still_to_top_right(position_played, players[0], players[1])
        players = self.check_nb_to_still_to_bottom_left(position_played, players[0], players[1])
        players = self.check_nb_to_still_to_bottom_right(position_played, players[0], players[1])

        return players

    def check_if_a_pawn_have_to_swap_team(self, player_who_played, player_to_check_pawn, position_played):

        player_who_played_start_copy = player_who_played
        player_to_check_pawn_start_copy = player_to_check_pawn

        player_who_played, player_to_check_pawn = self.swap_type_if_spawn_circled(player_who_played, player_to_check_pawn, position_played)

        if self.p1 == player_to_check_pawn_start_copy:
            self.p1 = player_to_check_pawn
            self.p2 = player_who_played
        else:
            self.p1 = player_who_played
            self.p2 = player_to_check_pawn

        return True

    def start_game(self):

        while not self.is_game_terminate():
            self.console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- "
                    + self.p1.name + " have to play (" + self.p1.symbol +
                    ") ---------------------------------------------------------------------\n"),
                justify="center", style="green"
            )

            self.print()

            if self.p1.type == "real":
                position_played = self.p1.play(self.map)
            else:
                position_played = self.p1.IA_play(self.map)
            self.update_map()
            self.check_if_a_pawn_have_to_swap_team(self.p1, self.p2, position_played)
            self.update_map()

            self.console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- "
                    + self.p2.name + " have to play (" + self.p2.symbol +
                    ") ---------------------------------------------------------------------\n"),
                justify="center", style="cyan"
            )

            self.print()

            if self.p2.type == "real":
                position_played = self.p2.play(self.map)
            else:
                position_played = self.p2.IA_play(self.map)
            self.update_map()
            self.check_if_a_pawn_have_to_swap_team(self.p2, self.p1, position_played)
            self.update_map()

    def is_game_terminate(self):
        return False
