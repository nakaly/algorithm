import math

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for i in range(lowLimit, highLimit+1):
            box_num = calcBox(i)
            num_of_balls = boxes.get(box_num)
            if num_of_balls is None:
                boxes[box_num] = 1
            else:
                boxes[box_num] = num_of_balls + 1
        # print(boxes)
        return max(boxes.values())



def calcBox(num: int) -> int:
    box_num = 0
    while num >= 1:
        box_num += num % 10
        num = math.floor(num / 10)
    return box_num

if __name__ == '__main__':
    print(Solution().countBalls(10008765, 100000000000))