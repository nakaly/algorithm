def part_one():
    num_of_increase = 0
    previous = None
    with open("./input/dayOne") as f:
        for line in f:
            depth = int(line)
            if previous != None and (depth - previous) > 0:
                num_of_increase += 1
            previous = depth
    print(num_of_increase)


def part_two():
    num_of_increase = 0
    previous = None
    window = []
    with open("./input/day1") as f:
        for line in f:
            depth = int(line)
            window.append(depth)
            if len(window) < 3:
                continue
            if len(window) > 3:
                window = window[1:]
            window_sum = sum(window)
            if previous != None and (window_sum - previous) > 0:
                num_of_increase += 1
            previous = window_sum
    print(num_of_increase)


def main():
    part_two()


if __name__ == "__main__":
    main()
