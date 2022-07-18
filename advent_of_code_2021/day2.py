
def part_two():
    horizontal_pos = 0
    depth = 0
    aim = 0
    with open("./input/day2") as f:
        for line in f:
#             print(line)
            command, steps = line.split()
            int_steps = int(steps)
            if command == "forward":
                horizontal_pos += int_steps
                depth += aim * int_steps
            elif command == "down":
                aim += int_steps
            elif command == "up":
                aim -= int_steps
#             print(horizontal_pos)
#             print(depth)
#             print(aim)
#             print("-----")

    return horizontal_pos * depth

def part_one():
    horizontal_pos = 0
    depth = 0
    with open("./input/day2") as f:
        for line in f:
            command, steps = line.split()
            int_steps = int(steps)
            if command == "forward":
                horizontal_pos += int_steps
            elif command == "down":
                depth += int_steps
            elif command == "up":
                depth -= int_steps
    return horizontal_pos * depth


def main():
    print(part_two())

if __name__ == "__main__":
    main()