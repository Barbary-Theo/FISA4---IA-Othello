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