from typing import List
from functools import cmp_to_key

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq_map = {}
        for n in nums:
            if n % 2 == 0:
                if n in freq_map:
                    freq_map[n] += 1
                else:
                    freq_map[n] = 1
        if bool(freq_map):
            return sorted(freq_map.items(),key=cmp_to_key(compare))[0][0]
        else:
            return -1

def compare(item1, item2):
    if item1[1] > item2[1]:
        return -1
    elif item1[1] < item2[1]:
        return 1
    else:
        if item1[0] > item2[0]:
            return 1
        elif item1[0] < item2[0]:
            return -1
        else:
            return 0



if __name__ == '__main__':
    print(Solution().mostFrequentEven([29,47,21,41,13,37,25,7]))