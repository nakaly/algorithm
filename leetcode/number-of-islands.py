
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        label_of_no_value = 100000
        labeled = [[label_of_no_value] * n for i in range(m)]
        num_of_islands = 0
        label_of_zero = 10000
        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                if value == "0":
                    labeled[i][j] = label_of_zero
                else:
                    if self.is_in_the_map(m,n,i-1,j) and self.is_in_the_map(m,n,i,j-1):
                        if labeled[i-1][j] < labeled[i][j-1]:
                            labeled[i][j] = labeled[i-1][j]
                            if labeled[i][j-1] != label_of_zero:
                                self.re_labeled(labeled[i-1][j], labeled[i][j-1], labeled, m, n)
                        elif labeled[i-1][j] > labeled[i][j-1]:
                            labeled[i][j] = labeled[i][j-1]
                            if labeled[i-1][j] != label_of_zero:
                                self.re_labeled(labeled[i][j-1], labeled[i-1][j], labeled, m, n)
                        else:
                            if labeled[i-1][j] != label_of_zero:
                                labeled[i][j] = labeled[i-1][j]
                            else:
                                num_of_islands += 1
                                labeled[i][j] = num_of_islands

                    elif self.is_in_the_map(m,n,i-1,j) and not self.is_in_the_map(m,n,i,j-1):
                        if labeled[i-1][j] != label_of_zero:
                            labeled[i][j] = labeled[i-1][j]
                        else:
                            num_of_islands += 1
                            labeled[i][j] = num_of_islands
                    elif not self.is_in_the_map(m,n,i-1,j) and self.is_in_the_map(m,n,i,j-1):
                        if labeled[i][j-1] != label_of_zero:
                            labeled[i][j] = labeled[i][j-1]
                        else:
                            num_of_islands += 1
                            labeled[i][j] = num_of_islands
                    else:
                        num_of_islands += 1
                        labeled[i][j] = num_of_islands
                print("check")
                print(num_of_islands)
                latest_num_of_island = 0
                for x in range(m):
                    for y in range(n):
                        if labeled[x][y] != label_of_zero and labeled[x][y] != label_of_no_value and latest_num_of_island < labeled[x][y]:
                            latest_num_of_island = labeled[x][y]
                num_of_islands = latest_num_of_island
                print(labeled)
                print(num_of_islands)
        return num_of_islands

    def is_in_the_map(self, m: int, n: int, i: int, j: int) -> bool:
        return 0 <= i < m and 0 <= j < n

    def re_labeled(self, new_value: int, old_value: int, labeled: List[List[int]], m: int, n:int):
        for i in range(m):
            for j in range(n):
                if labeled[i][j] == old_value:
                    labeled[i][j] = new_value

if __name__ == '__main__':
    print(Solution().numIslands(
        [["0","1","0","0","1","1","1","0","0","0","0","0","1","0","0","0","0","1","0","1"],
         ["1","0","1","0","0","1","1","0","0","1","0","1","0","1","0","1","1","0","0","0"],
         ["0","1","0","0","0","1","1","1","1","0","0","0","0","0","1","1","1","1","0","1"],
         ["1","1","0","0","0","1","1","0","0","0","1","1","1","0","0","1","0","1","1","0"],
         ["0","1","0","1","1","0","1","0","0","0","1","0","0","1","0","0","0","0","0","1"],
         ["1","0","0","1","0","1","0","0","0","1","1","0","1","0","0","1","0","0","0","0"],
         ["1","0","0","0","1","1","0","0","0","0","0","1","0","0","1","0","0","0","0","1"],
         ["1","0","0","0","1","0","1","1","1","0","1","0","1","1","1","1","0","0","0","1"],
         ["1","0","0","1","0","0","0","1","0","0","0","0","0","0","0","0","0","1","0","1"],
         ["0","0","0","1","0","1","1","1","1","1","1","1","1","1","0","0","0","0","1","0"],
         ["1","0","1","0","1","0","0","1","1","1","0","1","1","0","0","1","1","0","0","0"],
         ["0","1","0","0","1","0","0","0","0","0","0","1","1","1","1","0","0","0","1","0"],
         ["1","0","0","0","1","1","1","0","1","0","0","0","1","0","1","0","1","0","0","1"],
         ["0","0","0","0","1","0","1","1","0","1","0","1","0","1","1","1","1","0","0","0"],
         ["0","1","1","0","0","0","0","1","0","0","1","1","1","0","0","1","1","0","1","0"],
         ["1","0","1","1","1","1","1","1","0","1","1","0","1","0","0","1","0","0","0","1"],
         ["1","0","0","0","1","0","1","0","0","1","0","1","0","0","1","0","0","1","1","1"],
         ["0","0","1","0","0","0","0","1","0","0","1","1","0","1","1","1","0","0","0","0"],
         ["0","0","1","0","0","0","0","0","0","1","1","0","1","0","1","0","0","0","1","1"],
         ["1","0","0","0","1","0","1","1","1","0","0","1","0","1","0","1","1","0","0","0"]]
    ))
    # print(Solution().numIslands([
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]))