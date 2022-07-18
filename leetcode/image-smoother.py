
from typing import List
import math

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        x_lentgh = len(img)
        y_length = len(img[0])
        smoothed = []
        for i in range(x_lentgh):
            row = []
            for j in range(y_length):
                # print("i:",i,", j:", j)
                all = []
                for row_diff in [-1,0,1]:
                    for col_diff in [-1,0,1]:
                        if 0 <= i + row_diff < x_lentgh and 0 <= j + col_diff < y_length:
                            all.append(img[i+row_diff][j+col_diff])
                print(all)
                row.append(math.floor(sum(all) / len(all)))
            smoothed.append(row)
        return smoothed


if __name__ == '__main__':
    print(Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))