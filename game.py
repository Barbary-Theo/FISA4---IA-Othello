from rich.text import Text

from player import Player


class Game:

    def __init__(self, p1: Player = None, p2: Player = None, nb_row=8, nb_col=8):
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

        from rich import console
        console = console.Console()

        console.print("    ", end="")
        for i in range(len(self.map)):
            console.print("[red]" + str(i) + "[/]", style="underline", end="")
            console.print("  ", end="")

        console.print("")
        row_number = 0

        for row in self.map:
            string = "[red]" + str(row_number) + "|  " + "[/]"
            for col in row:
                string += str(col) + "  "
            row_number += 1
            console.print(string)

    def print_all(self):
        self.print()
        self.p1.print()
        self.p2.print()

    def update_map(self):
        for pawn in self.p1.pawn_set:
            self.map[pawn.get("x")][pawn.get("y")] = "o"

        for pawn in self.p2.pawn_set:
            self.map[pawn.get("x")][pawn.get("y")] = "x"

    def start_game(self):

        from rich import console
        console = console.Console()

        is_game_terminate = False

        while not is_game_terminate:
            console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- " + self.p1.name
                    + " have to play ---------------------------------------------------------------------\n"),
                justify="center", style="green"
            )

            self.print()

            if self.p1.type == "real":
                self.p1.play(self.map)
            else:
                self.p1.IA_play(self.map)
            self.update_map()

            console.print(
                Text(
                    "\n-------------------------------------------------------------------------------- " + self.p2.name
                    + " have to play ---------------------------------------------------------------------\n"),
                justify="center", style="cyan"
            )

            self.print()

            if self.p2.type == "real":
                self.p2.play(self.map)
            else:
                self.p2.IA_play(self.map)
            self.update_map()
