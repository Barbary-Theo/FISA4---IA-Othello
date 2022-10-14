
class Map:

    def __init__(self, nb_column = 8, nb_row = 8):
        self.nb_col = nb_column
        self.nb_row = nb_row
        self.map = self.init_map()

    def init_map(self):
        map = []
        for i in range(self.nb_row):
            row = []
            for j in range(self.nb_col):
                row.append(".")
            map.append(row)

        return map

    def print(self):

        from rich import console
        console = console.Console()

        console.print("    ", end="")
        for i in range(len(self.map)):
            console.print("[red]" + str(i) + "[/]", style="underline red", end="")
            console.print("  ", end="")

        console.print("")
        row_number = 0

        for row in self.map:
            string = "[red]" + str(row_number) + "|  " + "[/]"
            for col in row:
                string += str(col) + "  "
            row_number += 1
            console.print(string)
