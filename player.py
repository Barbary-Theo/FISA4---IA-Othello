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

    def play(self, map):

        is_a_good_placement = False

        while not is_a_good_placement:

            self.console.print("\nChoose a position to put your pawn", style="yellow")

            try:
                self.console.print("-> Column number : ", style="yellow", end="")
                x = int(input())
                self.console.print("-> Row number : ", style="yellow", end="")
                y = int(input())

                if x < 0 or y < 0:
                    self.console.print("Please check your inputs\n", style="red")
                elif self.exist_enemy_pawn_arround(map, {"x": x, "y": y}):
                    if map[y][x] == ".":
                        is_a_good_placement = True
                        self.pawn_set.append({"x": x, "y": y})
                        return {"x": x, "y": y}
                    else:
                        self.console.print("❌ Position already token ❌", style="red")
                        self.console.print()
                else:
                    self.console.print("❌ No pawn arround this position ❌", style="red")
                    self.console.print()

            except Exception:
                self.console.print("Please check your inputs\n", style="red")

    def ia_play(self, map):

        """
        TODO
            -> implement IA method to play
        """

        map.print()

        return {"x": -1, "y": -1}
