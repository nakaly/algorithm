
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        uniqeue_nums = nums
        lsh = []
        for candidate in uniqeue_nums:
            sh = []
            nums_in_sh = set()
            for num in nums:
                if (num - candidate) == 1 or num == candidate:
                     sh.append(num)
                     nums_in_sh.add(num)
            if len(lsh) < len(sh) and len(nums_in_sh) > 1:
                lsh = sh
        return len(lsh)



if __name__ == '__main__':
    print(Solution().findLHS([1,3,2,2,5,2,3,7]))