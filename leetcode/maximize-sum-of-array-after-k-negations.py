

from typing import List
import sys


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i = 0
        result = 0
        for num in nums:
            if num == 0 :
                i = k
            elif i < k:
                if num < 0:
                    result += -num
                else:
                    if (k - i) % 2 == 0:
                        result += num
                    else:
                        print("test" , -nums[i-1])
                        print("num", num)
                        print("aa", i-1)
                        if i-1 < 0:
                            result += -num
                            print("tt")
                        elif -nums[i-1] < num:
                            print("tt")
                            result -= (-nums[i-1] * 2)
                            result += num
                        else:
                            result += -num

                    i = k
            else:
                result += num
            i +=1
        return result


if __name__ == '__main__':
    print(Solution().largestSumAfterKNegations([4,2,3], 1))


