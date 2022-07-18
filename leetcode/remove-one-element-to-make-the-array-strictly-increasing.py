from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        i = 0
        while i < len(nums):
            # print("++++")
            # print("i", i)
            # print("i+1", i+1)
            if i+1 < len(nums) and nums[i] >= nums[i+1]:
                # print("i-1", i-1)
                # print("i+1", i+1)

                if removed:
                    return False
                if i-1 <0:
                    if i+2 < len(nums):
                        if nums[i] < nums[i+2]:
                            i += 2
                            removed = True
                        elif nums[i+1] < nums[i+2]:
                            i += 1
                            removed = True
                        else:
                            return False
                    else:
                        i += 1
                        removed = True
                else:
                    if nums[i-1] < nums[i+1]:
                        i += 1
                        removed = True
                    elif i+2 < len(nums):
                        if nums[i] < nums[i+2]:
                            i += 2
                            removed = True
                        elif nums[i - 1] < nums[i + 1] < nums[i + 2]:
                            i += 1
                            removed = True
                        else:
                            return False
                    else:
                        i += 1
                        removed = True
            else:
                i+=1
            # print("====")
        return True



if __name__ == '__main__':
    print(Solution().canBeIncreasing([1,2,10,5,7]))