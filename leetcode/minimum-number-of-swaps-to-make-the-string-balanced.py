
from typing import List

class Solution:
    def minSwaps(self, s: str) -> int:
        ope_count = 0
        swap_index = isBalanced(s, 0, len(s)-1)
        s = list(s)
        while len(swap_index) > 0:
            print(swap_index)
            ope_count += 1
            # s[swap_index[0]], s[swap_index[1]] = s[swap_index[1]], s[swap_index[0]]
            swap_index = isBalanced(s, swap_index[0]+1, swap_index[1]-1)

        return ope_count




def isBalanced(s: str, start: int, end: int) -> List:
    num_if_left = 0
    for i in range(start, end+1):
        if s[i] == '[':
            num_if_left +=1
        elif s[i] == ']':
            if num_if_left > 0:
                num_if_left -=1
            else:
                num_of_right = 0
                for j in range(end, i, -1):
                    if s[j] == ']':
                        num_of_right+1
                    elif s[j] == '[':
                        if num_of_right > 0:
                            num_of_right -=1
                        else:
                            return [i,j]
                    if i == j:
                        return []
        if i == end:
            return []

    return []

if __name__ == '__main__':
    print(Solution().minSwaps("]]][[["))