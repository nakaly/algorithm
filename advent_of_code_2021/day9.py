
def part_one():
    positions = []
    with open("./input/day9") as f:
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(int(char))
            positions.append(row)

    risk_level = 0
    max_y = len(positions)
    max_x = len(positions[0])
    for i in range(max_y):
        for j in range(max_x):
            adjacents = []
            for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                p, q = move
                x = j + q
                y = i + p
                # print("x:", x, "y:", y)
                if (0 <= x < max_x) and (0 <= y < max_y):
                    adjacents.append(positions[y][x])
            # print(adjacents)
            if all(map(lambda x: positions[i][j] < x, adjacents)):
                # print("j:", j, "i:", i)
                risk_level += (positions[i][j] + 1)
    return risk_level

def part_two():
    positions = []
    with open("./input/day9") as f:
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(int(char))
            positions.append(row)

    top_three = []
    marked = {}
    max_y = len(positions)
    max_x = len(positions[0])
    for i in range(max_y):
        for j in range(max_x):
            marked[(j,i)] = False

    for i in range(max_y):
        for j in range(max_x):
            adjacents = []
            for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                p, q = move
                x = j + q
                y = i + p
                # print("x:", x, "y:", y)
                if (0 <= x < max_x) and (0 <= y < max_y):
                    adjacents.append(positions[y][x])
            # print(adjacents)
            if all(map(lambda x: positions[i][j] < x, adjacents)):
                # print("j:", j, "i:", i)
                marked[(j,i)] = True



# def find_basin(x, y, positions, marked):



def main():
    print(part_one())


if __name__ == "__main__":
    main()