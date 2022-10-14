from rich import console

class Player:

    console = console.Console()

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
        set = ""
        for object in self.pawn_set:
            set += "\n    {x: \"" + str(object.get("x")) + "\", y: \"" + str(object.get("y")) + "\"}"

        self.console.print(
            "player { \n  name: \"" + self.name + "\",\n  couleur: \"" + self.couleur + "\"\n  pawn: [" + set + "\n  ]\n}")

    def play(self, map):

        is_a_good_placement = False

        while not is_a_good_placement:

            self.console.print("\nChoose a position to put your pawn", style="yellow")
            try:
                self.console.print("-> Column number : ", style="yellow", end="")
                y = int(input())
                self.console.print("-> Row number : ", style="yellow", end="")
                x = int(input())
                nice_input = True

            except Exception as e:
                nice_input = False
                x= 3
                y = 3

            if nice_input:
                try:
                    if map[x][y] == ".":
                        is_a_good_placement = True
                        self.pawn_set.append({"x": x, "y": y})
                    else:
                        self.console.print("❌ Position already token ❌", style="red")
                        self.console.print()
                except Exception as e:
                    self.console.print("Please check your inputs\n", style="red")
            else:
                self.console.print("Please check your inputs\n", style="red")

    def IA_play(self, map):
        self.console.print("\n⚠️Functionality to develop ⚠️\n", style="red")
