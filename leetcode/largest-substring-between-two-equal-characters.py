
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        char_map = {}
        for c in s:
            if c in char_map:
                length_between = char_map[c]
                result = max(result, length_between)
                char_map[c] += 1
            else:
                char_map[c] = 0
            for k in char_map.keys():
                if k != c:
                    char_map[k] += 1
            # print(char_map)
        return result



if __name__ == '__main__':
    print(Solution().maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))