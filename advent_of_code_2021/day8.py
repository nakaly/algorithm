
def part_one():
    with open("./input/day8") as f:
        count = 0
        for line in f:
            sample, output = line.split("|")
            four_digits = output.split(" ")
            num_of_1478 = sum(map(lambda x: 1 if x in [2,3,4,7] else 0, map(lambda x: len(x), map(lambda x: x.rstrip(), four_digits))))
            count += num_of_1478
        return count

def part_two():
    with open("./input/day8") as f:

        display_digit = {"abcefg" : 0, "cf": 1, "acdeg": 2, "acdfg":3, "bcdf":4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg":9 }
        total = 0
        for line in f:
            translation = {}
            sample, output = line.rstrip().split("|")
            samples = sample.split(" ")
            one = list(filter(lambda x : len(x) == 2, samples))[0]
            four = list(filter(lambda x : len(x) == 4, samples))[0]
            seven = list(filter(lambda x : len(x) == 3, samples))[0]
            eight = list(filter(lambda x : len(x) == 7, samples))[0]

            all_chars = list(filter(lambda x: x != ' ', [c for c in sample]))
            char_stats = {all_chars.count(x):x for x in all_chars}
            # print(char_stats)
            translated_e = char_stats.get(4)
            translation[char_stats.get(4)] = 'e'
            translated_b = char_stats.get(6)
            translation[char_stats.get(6)] = 'b'
            translated_f = char_stats.get(9)
            translation[char_stats.get(9)] = 'f'

            translated_a = list(filter(lambda x: not x in one, seven))[0]
            translation[list(filter(lambda x: not x in one, seven))[0]] = 'a'
            translated_c = list(filter(lambda x: x != translated_f, one))[0]
            translation[list(filter(lambda x: x != translated_f, one))[0]] = 'c'

            translated_d = list(filter(lambda x: not x in [translated_b, translated_c, translated_f], four))[0]
            translation[list(filter(lambda x: not x in [translated_b, translated_c, translated_f], four))[0]] = 'd'
            translated_g = list(filter(lambda x: not x in translation.keys(), eight))[0]
            translation[list(filter(lambda x: not x in translation.keys(), eight))[0]] = 'g'

            # print(translated_a, translated_b, translated_c, translated_d, translated_e, translated_f, translated_g)

            four_digits = output.split(" ")[1:]
            output_value = 0
            # print(four_digits)
            # print(translation)
            output_value += display_digit.get("".join(sorted(list(map(lambda x: translation.get(x), four_digits[0]))))) * 1000
            output_value += display_digit.get("".join(sorted(list(map(lambda x: translation.get(x), four_digits[1]))))) * 100
            output_value += display_digit.get("".join(sorted(list(map(lambda x: translation.get(x), four_digits[2]))))) * 10
            output_value += display_digit.get("".join(sorted(list(map(lambda x: translation.get(x), four_digits[3])))))
            total += output_value
        return total



def main():
    print(part_two())


if __name__ == "__main__":
    main()