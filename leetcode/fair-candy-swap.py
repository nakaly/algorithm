from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceTotal = 0
        aliceBoxes = set()
        for item in aliceSizes:
            aliceBoxes.add(item)
            aliceTotal += item
        bobTotal = 0
        bobBoxes = set()
        for item in bobSizes:
            bobBoxes.add(item)
            bobTotal += item
        isBobBigger = False
        if aliceTotal < bobTotal:
            isBobBigger = True
            diff = (bobTotal - aliceTotal) // 2
        else:
            diff = (aliceTotal - bobTotal) // 2
        for item in aliceSizes:
            if isBobBigger:
                if item + diff in bobBoxes:
                    return [item, item+diff]
            else:
                if item - diff in bobBoxes:
                    return [item, item-diff]






if __name__ == '__main__':
    print(Solution().fairCandySwap([1,1],[2,2]))

