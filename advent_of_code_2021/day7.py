import math
import sys

def part_one():
    with open("./input/day7") as f:
        line = f.readline()
        positions = list(map(lambda x: int(x), line.split(",")))
        positions.sort()
        # print(positions)
        length = len(positions)
        half = math.floor(length / 2)
        median = positions[half]
        # print(median)
        total = 0
        for pos in positions:
            cost = abs(pos - median)
            total += math.floor(cost * (cost + 1) / 2)
        return total


def part_two():
    with open("./input/day7") as f:
        line = f.readline()
        positions = list(map(lambda x: int(x), line.split(",")))
        # positions.sort()
        # print(positions)
        length = len(positions)
        average = sum(positions)/length
        average_pos = 475
        average_diff = abs(average - average_pos)
        print(average)
        # for pos in positions:
        #     diff = abs(average - pos)
        #
        #     if average_diff > diff:
        #         average_diff = diff
        #         average_pos = pos
        total = 0
        print(average_pos)
        for pos in positions:
            cost = abs(pos - average_pos)
            total += (cost * (cost + 1) / 2)
        return total


def calc_cost(value, positions):
    total = 0
    for pos in positions:
        cost = abs(pos - value)
        total += math.floor(cost * (cost + 1) / 2)
    return total


def main():
    print(part_two())


if __name__ == "__main__":
    main()