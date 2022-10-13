
class Player:

    def __init__(self, name: str = None, couleur: str = "white", pawn_set: list = None):
        if pawn_set is None:
            pawn_set = []
        self.name = name
        self.couleur = couleur
        self.pawn_set = pawn_set


    def __str__(self):

        set = ""
        for object in self.pawn_set:
            set += "\n\t\t{x: \"0.0\", y: \"0.0\"}"

        return "player { \n\tname: \"" + self.name + "\",\n\tcouleur: \"" + self.couleur +"\"\n\tpawn: ["+ set +"\n\t]\n}"
