import math

def part_one():
    count = 0
    with open("./input/day6") as f:
        line = f.readline()
        state = list(map(lambda x: int(x), line.split(",")))
        count += len(state)
        for day in range(80):
            length = len(state)
            for i in range(length):
                if state[i] == 0:
                    state.append(8)
                    state[i] = 6
                    count += 1
                else:
                    state[i] -= 1
    return count


dp = [0 for i in range(256)]


def part_two():
    count = 0
    days = 256
    with open("./input/day6") as f:
        line = f.readline()
        state = list(map(lambda x: int(x), line.split(",")))

        count = sum(map(lambda x: num_of_descendants(days - x), state))

    return count


def num_of_descendants(remaining_days):
    total = 1
    if remaining_days - 1 < 0:
        return total
    if dp[remaining_days] != 0:
        return dp[remaining_days]

    num_of_children = math.floor((remaining_days - 1) / 7) + 1

    for i in range(num_of_children):
        remaining_for_child = remaining_days - 9 - 7 * i
        total += num_of_descendants(remaining_for_child)


    dp[remaining_days] = total
    return total


def main():
    print(part_two())


if __name__ == "__main__":
    main()
