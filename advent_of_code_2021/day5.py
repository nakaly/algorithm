def part_one():
    points = [[0 for j in range(1000)] for i in range(1000)]
    score = 0
    with open("./input/day5") as f:
        for line in f:
            first, middle, second = line.split(" ")
            x1, y1 = list(map(lambda x : int(x), first.split(",")))
            x2, y2 = list(map(lambda x : int(x), second.split(",")))
            if x1 == x2:
                if y1 <= y2:
                    for i in range(y1, y2+1):
                        if points[x1][i] == 1:
                            score += 1
                        points[x1][i] += 1
                else:
                    for i in range(y2, y1+1):
                        if points[x1][i] == 1:
                            score += 1
                        points[x1][i] += 1
            elif y1 == y2:
                if x1 <= x2:
                    for i in range(x1, x2+1):
                        if points[i][y1] == 1:
                            score += 1
                        points[i][y1] += 1
                else:
                    for i in range(x2, x1+1):
                        if points[i][y1] == 1:
                            score += 1
                        points[i][y1] += 1
            elif abs((y2 - y1) / (x2 - x1)) == 1:
                if x1 <= x2 and y1 <= y2:
                    for i in range((x2 - x1)+1):
                        if points[x1 + i][y1 + i] == 1:
                            score += 1
                        points[x1 + i][y1 + i] += 1
                elif x1 <= x2 and y1 > y2:
                    for i in range((x2 - x1)+1):
                        if points[x1 + i][y1 - i] == 1:
                            score += 1
                        points[x1 + i][y1 - i] += 1
                if x1 > x2 and y1 <= y2:
                    for i in range((x1 - x2)+1):
                        if points[x2 + i][y2 - i] == 1:
                            score += 1
                        points[x2 + i][y2 - i] += 1
                elif x1 > x2 and y1 > y2:
                    for i in range((x1 - x2)+1):
                        if points[x2 + i][y2 + i] == 1:
                            score += 1
                        points[x2 + i][y2 + i] += 1
    # print_points(points)
    return score


def print_points(points):
    length = len(points)
    for i in range(length):
        for j in range(length):
            print(points[j][i], end="")
        print("")


def main():
    print(part_one())


if __name__ == "__main__":
    main()