
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}
        for word in words:
            for c in word:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1
        num_of_words = len(words)
        return all(map(lambda x: x % num_of_words == 0, freq.values()))


if __name__ == '__main__':
    print(Solution().makeEqual(["abc","aabc","bc"]))