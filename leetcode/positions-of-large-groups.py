from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = []
        start = -1
        end = -1
        current = None
        for i in range(0, len(s)):
            # print("current", current)
            # print("i", i)
            # print("s[i]", s[i])
            if current != s[i]:
                if current != None:
                    end = i-1
                    # print("start",start)
                    # print("end", end)
                    if end - start >= 2:
                        answer.append([start, end])
                start = i
            current = s[i]
        if len(s)-1 - start >= 2:
            answer.append([start, len(s)-1])
        return answer



if __name__ == '__main__':
    print(Solution().largeGroupPositions("aaa"))