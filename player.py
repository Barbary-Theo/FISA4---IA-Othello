from rich.markdown import Markdown


class Player:

    def __init__(self, name: str = None, couleur: str = "white", pawn_set: list = None):
        if pawn_set is None:
            pawn_set = []
        self.name = name
        self.couleur = couleur
        self.pawn_set = pawn_set

    def print(self):

        from rich import console
        console = console.Console()

        set = ""
        for object in self.pawn_set:
            set += "\n    {x: \"" + str(object.get("x")) + "\", y: \"" + str(object.get("y")) + "\"}"

        console.print(
            "player { \n  name: \"" + self.name + "\",\n  couleur: \"" + self.couleur + "\"\n  pawn: [" + set + "\n  ]\n}")

    def play(self, map):
        from rich import console
        console = console.Console()

        is_a_good_placement = False

        while not is_a_good_placement:

            try:
                console.print("Column : ", style="yellow", end="")
                x = int(input())
                console.print("Row : ", style="yellow", end="")
                y = int(input())
                nice_input = True

            except Exception as e:
                nice_input = False
                y = 3
                x = 3

            if nice_input:
                try:
                    if map[y][x] == ".":
                        is_a_good_placement = True
                        self.pawn_set.append({"x": x, "y": y})
                    else:
                        console.print("x Position already token x", style="red")
                        console.print()
                except Exception as e:
                    console.print("Please check your inputs\n", style="red")
            else:
                console.print("Please check your inputs\n", style="red")

