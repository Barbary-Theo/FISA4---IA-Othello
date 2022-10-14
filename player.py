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

        console.print( "player { \n  name: \"" + self.name + "\",\n  couleur: \"" + self.couleur + "\"\n  pawn: [" + set + "\n  ]\n}")
