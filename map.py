
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
                row.append(0)
            map.append(row)

        return map

    def __str__(self):

        string = "\t"
        for i in range(len(self.map)):
            string += str(i) + "\t"
        string += "\n\t"
        for row in self.map:
            string += "_\t"
        string += "\n"

        row_number = 0

        for row in self.map:
            string += str(row_number) + "|\t"
            for col in row:
                string += str(col) + "\t"
            string += "\n"
            row_number += 1

        return string
