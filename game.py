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

    def is_pawn_embrassed(self, position: dict, symbol: str):
        return (
                (self.map[position.get("x") - 1][position.get("y")] == symbol
                 and self.map[position.get("x") + 1][position.get("y")] == symbol)
                or
                (self.map[position.get("x")][position.get("y") - 1] == symbol
                 and self.map[position.get("x")][position.get("y") + 1] == symbol)
                or
                (self.map[position.get("x") - 1][position.get("y") - 1] == symbol
                 and self.map[position.get("x") + 1][position.get("y") + 1] == symbol)
                or
                (self.map[position.get("x") - 1][position.get("y") + 1] == symbol
                 and self.map[position.get("x") + 1][position.get("y") - 1] == symbol)
        )

    def is_a_pawn_have_to_swap_team(self, player_who_played, player_to_check_pawn):

        player_who_played_start_copy = player_who_played
        player_to_check_pawn_start_copy = player_to_check_pawn

        for position in player_to_check_pawn.pawn_set:

            try:
                if self.is_pawn_embrassed(position, player_who_played.symbol):
                    player_to_check_pawn.pawn_set.remove(position)
                    player_who_played.pawn_set.append(position)
            except Exception as e:
                self.console.print(e + " -> ? index out of bounds ? ", style="red")

        if self.p1 == player_to_check_pawn_start_copy:
            self.p1 = player_who_played
            self.p2 = player_to_check_pawn
        else:
            self.p1 = player_who_played
            self.p2 = player_to_check_pawn

        return True

    def start_game(self):

        is_game_terminate = False

        while not is_game_terminate:
            self.console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- "
                    + self.p1.name + " have to play (" + self.p1.symbol +
                    ") ---------------------------------------------------------------------\n"),
                justify="center", style="green"
            )

            self.print()

            if self.p1.type == "real":
                self.p1.play(self.map)
            else:
                self.p1.IA_play(self.map)
            self.update_map()
            self.is_a_pawn_have_to_swap_team(self.p1, self.p2)
            self.is_a_pawn_have_to_swap_team(self.p2, self.p1)
            self.update_map()

            self.console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- "
                    + self.p2.name + " have to play (" + self.p1.symbol +
                    ") ---------------------------------------------------------------------\n"),
                justify="center", style="cyan"
            )

            self.print()

            if self.p2.type == "real":
                self.p2.play(self.map)
            else:
                self.p2.IA_play(self.map)
            self.update_map()
            self.is_a_pawn_have_to_swap_team(self.p1, self.p2)
            self.is_a_pawn_have_to_swap_team(self.p2, self.p1)
            self.update_map()

