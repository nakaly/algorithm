from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top_three = set()
        for n in nums:
            if n in top_three:
                continue
            if len(top_three) < 3:
                top_three.add(n)
            else:
                min_in_top_three = min(top_three)
                if n > min_in_top_three:
                    top_three.remove(min_in_top_three)
                    top_three.add(n)
        if len(top_three) < 3:
            return max(top_three)
        else:
            return min(top_three)

if __name__ == '__main__':
    print(Solution().thirdMax([1,2,2,5,3,5]))