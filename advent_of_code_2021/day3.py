import copy


def part_one():
    bits_summary = []
    num_of_digit = 0
    with open("./input/day3") as f:
        for line in f:
            for i, zero_or_one in enumerate(line):
                if i == len(line) - 1:
                    continue
                is_zero = "0" == zero_or_one
                if len(bits_summary) <= i:
                    zero_one_sum = [1 if is_zero else 0, 0 if is_zero else 1]
                    bits_summary.append(zero_one_sum)
                    num_of_digit += 1
                else:
                    bits_summary[i][0 if is_zero else 1] += 1
                # print("-----")
                # print(bits_summary)
    # print(bits_summary)
    # print(num_of_digit)
    gamma = 0
    epsilon = 0
    for i, bit in enumerate(bits_summary):
        value = 2 ** (num_of_digit - i - 1)
        # print(value)
        if bit[0] < bit[1]:
            gamma += value
        else:
            epsilon += value
    #
    # print("gammna", gamma)
    # print("epsilon", epsilon)
    return gamma * epsilon


def part_two():
    bits_summary = []
    num_of_digit = 0
    numbers = []
    with open("./input/day3") as f:
        for line in f:
            num_of_digit = len(line)
            numbers.append(int(line, 2))
    o2_rate = copy.copy(numbers)
    num_of_bit = 0
    while len(o2_rate) > 1 and num_of_bit < num_of_digit:
        num_of_zero = 0
        num_of_one = 1
        for num in o2_rate:
            bit_mask = 2 ** (num_of_digit - num_of_bit - 1)
            if num & bit_mask > 0:
                num_of_one += 1
            else:
                num_of_zero += 1
        next_o2_rate = []
        for num in o2_rate:
            if num_of_zero < num_of_one:
                if num & bit_mask > 0:
                    next_o2_rate.append(num)
            else:
                if num & bit_mask == 0:
                    next_o2_rate.append(num)
        o2_rate = next_o2_rate
        num_of_bit += 1
    co2_rate = copy.copy(numbers)
    num_of_bit = 0
    while len(co2_rate) > 1 and num_of_bit < num_of_digit:
        num_of_zero = 0
        num_of_one = 1
        for num in co2_rate:
            bit_mask = 2 ** (num_of_digit - num_of_bit - 1)
            if num & bit_mask > 0:
                num_of_one += 1
            else:
                num_of_zero += 1
        next_co2_rate = []
        for num in co2_rate:
            if num_of_zero >= num_of_one:
                if num & bit_mask > 0:
                    next_co2_rate.append(num)
            else:
                if num & bit_mask == 0:
                    next_co2_rate.append(num)
        co2_rate = next_co2_rate
        num_of_bit += 1
    return o2_rate[0] * co2_rate[0]

def main():
    print(part_two())


if __name__ == "__main__":
    main()
