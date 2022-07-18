from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        char_indexes = defaultdict(list)
        for i, c in enumerate(s):
            char_indexes[c].append(i)

        # print(char_indexes)

        result = 0
        for k, v in char_indexes.items():
            print("k:", k, "v:", v)
            for i, index in enumerate(v):
                if i != 0:
                    left = index - v[i-1]
                else:
                    left = index + 1

                if i != len(v)-1:
                    right = v[i+1] - index
                else:
                    right = len(s) - index
                print("l:", left, "r:", right)
                tmp = left * right

                print(tmp)
                result += left * right

        return result
        # l = len(s)
        # score = 0
        # memo = {}
        # memo_duplicate = {}
        # for i in range(l, -1, -1):
        #     once = set()
        #     duplicate = set()
        #     for j in range(i,l):
        #         # print("subscring:", s[i:j+1])
        #         # print(memo)
        #         if (i+1,j) in memo:
        #             # print("from memo:i=", i+1, ", j=", j)
        #             once = copy.copy(memo[(i+1,j)])
        #             duplicate = copy.copy(memo_duplicate[(i+1,j)])
        #             if s[i] in once:
        #                 once.remove(s[i])
        #                 duplicate.add(s[i])
        #             elif not s[i] in duplicate:
        #                 once.add(s[i])
        #             memo[(i,j)] = once
        #             memo_duplicate[(i,j)] = duplicate
        #             score += len(once)
        #             continue
        #         if s[j] in once:
        #             once.remove(s[j])
        #             duplicate.add(s[j])
        #         elif not s[j] in duplicate:
        #             once.add(s[j])
        #         memo[(i,j)] = once
        #         memo_duplicate[(i,j)] = duplicate
        #         # print("once", once)
        #         # print("once", duplicate)
        #         score += len(once)
        #         # print(memo)
        # return score




if __name__ == '__main__':
    print(Solution().uniqueLetterString("LEETCODE"))