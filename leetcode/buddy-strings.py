
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_len = len(s)
        goal_len = len(goal)
        if s_len != goal_len:
            return False
        diff = set()
        all_chars = set()
        for i in range(s_len):
            if s[i] != goal[i]:
                diff.add(i)
            all_chars.add(goal[i])
        diff_size = len(diff)
        num_of_chars = len(all_chars)
        # print(diff)
        # print(all_chars)
        if diff_size == 0:
            if num_of_chars < s_len:
                return True
            else:
                return False
        if diff_size != 2:
            return False
        i = diff.pop()
        j = diff.pop()
        if i > j:
            tmp = i
            i = j
            j = tmp
        swapped = s[0:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        # print(swapped)
        if swapped == goal:
            return True
        return False




if __name__ == '__main__':
    # print(Solution().buddyStrings("ab","ba"))
    # print(Solution().buddyStrings("ab","ab"))
    # print(Solution().buddyStrings("aa","aa"))
    print(Solution().buddyStrings("aaaaaaabc","aaaaaaacb"))