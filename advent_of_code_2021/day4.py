def part_one():
    numbers = []
    boards = []
    with open("./input/day4") as f:
        is_first = True
        line = f.readline()
        while True:
            line = line.rstrip()
            if is_first:
                if line == "":
                    is_first = False
                    line = f.readline()
                else:
                    numbers = list(map(lambda x: int(x), line.split(",")))
                    line = f.readline()
            else:
                board = []
                while line != "\n" and line != "":
                    line = line.rstrip()
                    row = list(map(lambda x: Grid(int(x)), line.split()))
                    board.append(row)
                    line = f.readline()

                boards.append(Board(board))
                line = f.readline()
            if not line:
                break
    # print("numbers: ", numbers)
    # for b in boards:
    #     b.print()
    #     print("-----")

    # for called_num in [22,8,21,6,1]:
    #     boards[0].mark(called_num)
    # is_win, score = boards[0].is_win()
    # print(is_win)
    # print(score)
    # print(boards[0].print())

    for num in numbers:
        # print("called: ", num)
        for b in boards:
            b.mark(num)

            # b.print()
            # print("------")
        for i, b in enumerate(boards):
            is_win, score = b.is_win()
            if is_win:
                # print("win")
                # b.print()
                if len(boards) > 1:
                    boards.pop(i)
                    continue
                # print("last num: ", num)
                # print("score: ", score)
                return num * score
    return 0


class Grid:
    def __init__(self, value):
        self.value = value
        self.isMarked = False

    def print(self):
        print("(", self.value, ",", self.isMarked, ")", end="")


class Board:
    def __init__(self, grids):
        # grids is two dimensional array of grids
        self.grids = grids

    def mark(self, called_number):
        for line in self.grids:
            for grid in line:
                if grid.value == called_number:
                    grid.isMarked = True

    def is_win(self):
        for row in self.grids:
            is_win = all(map(lambda x: x.isMarked, row))
            if is_win:
                return is_win, self.score()
        for i in range(5):
            column = [self.grids[j][i] for j in range(5)]
            is_win = all(map(lambda x: x.isMarked, column))
            if is_win:
                return is_win, self.score()
        return False, []

    def print(self):
        for row in self.grids:
            for grid in row:
                grid.print()
            print("")

    def score(self):
        score = 0
        for row in self.grids:
            score += sum(map(lambda y: y.value, filter(lambda x: not x.isMarked, row)))
        return score


def main():
    print(part_one())


if __name__ == "__main__":
    main()
