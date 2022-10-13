
def create_map(nb_col, nb_line):
    map = []
    for i in range(nb_line):
        row = []
        for j in range(nb_col):
            row.append(0)
        map.append(row)

    return map


def display_map(map):

    print("\t", end="")
    for i in range(len(map)):
        print(i, end="\t")
    print("\n\t", end="")
    for row in map:
        print("_", end="\t")
    print("")

    row_number = 0

    for row in map:
        print(row_number, "|", end="\t")
        for col in row:
            print(col, end="\t")
        print("")
        row_number += 1

def prog():
    display_map(create_map(8, 8))


if __name__ == "__main__":
    prog()
