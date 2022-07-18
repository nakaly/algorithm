from typing import List

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:


def subsequence(list: List[int]):

    first_item = list[0]
    if len(list) == 1:
        return [[first_item],[]]
    result_of_the_rest = subsequence(list[1:])
    result = []
    for sub in result_of_the_rest:
        if len(sub) == 0:
            result.append([first_item])
        elif first_item < sub[0]:
            extended = [first_item]
            extended.extend(sub)
            result.append(extended)
    result.extend(result_of_the_rest)
    return result

if __name__ == '__main__':
    print(subsequence([10,9,2,5,3,7,101,18]))

