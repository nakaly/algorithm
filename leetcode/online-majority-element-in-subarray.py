from typing import List


class MajorityChecker:


    def __init__(self, arr: List[int]):
        self.array  = arr


    def query(self, left: int, right: int, threshold: int) -> int:
        occurrenceMap = {}
        subarray = self.array[left:right+1]
        for num in subarray:
            current = occurrenceMap.get(num)
            if current is None:
                occurrenceMap[num] = 1
            else:
                occurrenceMap[num] = current + 1
        for num, occurrence in occurrenceMap.items():
            if occurrence >= threshold:
                return num
        return -1


if __name__ == '__main__':
    checker = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(checker.query(0,5,4))
    print(checker.query(0,3,3))
    print(checker.query(2,3,2))
