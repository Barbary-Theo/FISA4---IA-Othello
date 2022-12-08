from rich.text import Text
from player import Player
from rich import console


class Game:
    console = console.Console()

    def __init__(self, p1: Player = None, p2: Player = None,
                 nb_row=8, nb_col=8,
                 depth=2):

        self.p1 = p1
        self.p2 = p2
        self.map = self.init_map(nb_row, nb_col)
        self.depth = depth

    def init_map(self, nb_row, nb_col):
        map_creation = []
        for i in range(nb_row):
            row = []
            for j in range(nb_col):
                if self.p1.pawn_set.__contains__({"x": j, "y": i}):
                    row.append("o")
                elif self.p2.pawn_set.__contains__({"x": j, "y": i}):
                    row.append("x")
                else:
                    row.append(".")
            map_creation.append(row)

        return map_creation

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
            self.map[pawn.get("y")][pawn.get("x")] = "o"

        for pawn in self.p2.pawn_set:
            self.map[pawn.get("y")][pawn.get("x")] = "x"

    def can_we_check_next_case(self, direction_x, direction_y, index_x, index_y):

        x_valid_to_check_next_case = True
        y_valid_to_check_next_case = True

        if direction_x < 0:
            x_valid_to_check_next_case = index_x >= 0
        if direction_y < 0:
            y_valid_to_check_next_case = index_y >= 0
        if direction_x > 0:
            x_valid_to_check_next_case = index_x < len(self.map[0]) - 2
        if direction_y > 0:
            y_valid_to_check_next_case = index_y < len(self.map) - 2

        return x_valid_to_check_next_case and y_valid_to_check_next_case

    def check_pawn_to_still_by_value(self, position_played, player_who_played, player_to_check, direction_x, direction_y):
        index_x = int(position_played.get("x")) + direction_x
        index_y = int(position_played.get("y")) + direction_y
        position_to_swap = []

        we_can_check_next_case = self.can_we_check_next_case(direction_x, direction_y, index_x, index_y)

        while we_can_check_next_case and self.map[index_y][index_x] == player_to_check.symbol:
            position_to_swap.append({"x": index_x, "y": index_y})
            index_x = index_x - 1 if direction_x < 0 else index_x
            index_x = index_x + 1 if direction_x > 0 else index_x
            index_y = index_y - 1 if direction_y < 0 else index_y
            index_y = index_y + 1 if direction_y > 0 else index_y

            we_can_check_next_case = self.can_we_check_next_case(direction_x, direction_y, index_x, index_y)

        try:
            if self.map[index_y][index_x] == player_who_played.symbol:
                for position in position_to_swap:
                    player_to_check.pawn_set.remove(position)
                    player_who_played.pawn_set.append(position)
        except Exception:
            pass

        return player_who_played, player_to_check


    def swap_type_if_spawn_circled(self, player_who_played, player_to_check_pawn, position_played):

        directions_to_check = [-1, 0, 1]
        players = [player_who_played, player_to_check_pawn]

        for direction_to_check in directions_to_check:
            for direction_to_check_bis in directions_to_check:

                if not (direction_to_check == 0 and direction_to_check_bis == 0):
                    players = self.check_pawn_to_still_by_value(position_played, players[0], players[1],
                                                                direction_to_check, direction_to_check_bis)

        return players

    def check_if_a_pawn_have_to_swap_team(self, player_who_played, player_to_check_pawn, position_played):

        player_to_check_pawn_start_copy = player_to_check_pawn
        nb_pawn_at_start = len(player_who_played.pawn_set)

        player_who_played, player_to_check_pawn = self.swap_type_if_spawn_circled(player_who_played, player_to_check_pawn, position_played)

        if self.p1 == player_to_check_pawn_start_copy:
            self.p1 = player_to_check_pawn
            self.p2 = player_who_played
        else:
            self.p1 = player_who_played
            self.p2 = player_to_check_pawn


        nb_pawn_stolen = len(player_who_played.pawn_set) - nb_pawn_at_start
        return nb_pawn_stolen

    def start_game(self):

        position_error = {"x": -1, "y": -1}

        while True:
            self.console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- "
                    + self.p1.name + " have to play (" + self.p1.symbol +
                    ") ---------------------------------------------------------------------\n"),
                justify="center", style="green"
            )

            self.print()

            if self.p1.type == "real":
                position_played = self.p1.play(self.map, self.p2)
            else:
                position_played = self.p1.ia_play(self.map, self.p2, self.depth)

            if position_played == position_error:
                break

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
                position_played = self.p2.play(self.map, self.p1)
            else:
                position_played = self.p2.ia_play(self.map, self.p1, self.depth)

            if position_played == position_error:
                break

            self.update_map()
            self.check_if_a_pawn_have_to_swap_team(self.p2, self.p1, position_played)
            self.update_map()

        self.console.print("Fin de partie", style="red")
