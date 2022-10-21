from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        first = True
        for word in words:
            if first:
                result = list(word)
                first = False
            else:
                print(result, word)
                next_result = []
                for char in word:
                    if char in result:
                        next_result.append(char)
                        result.remove(char)

                result = next_result

        return result

if __name__ == '__main__':
    print(Solution().commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]))