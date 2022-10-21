from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        rotated = mat
        for i in range(3):
            rotated = rotate(rotated)
            if rotated == target:
                return True
        return False


def rotate(mat: List[List[int]]) -> List[List[int]]:
    length = len(mat)
    rotated = [[0]*length for i in range(length)]
    for i in range(length):
        for j in range(length):
            rotated[i][j] = mat[length - j - 1][i]
    return rotated


if __name__ == '__main__':
    print(Solution().findRotation([[0,1],[1,0]], [[1,0],[0,1]]))