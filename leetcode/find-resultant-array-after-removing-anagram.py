import collections
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        modified = True
        while modified:
            modified = False
            new_words = [words[0]]
            for i in range(1,len(words)):
                freq_chars_prev = collections.Counter(words[i-1])
                freq_char = collections.Counter(words[i])
                if freq_chars_prev == freq_char:
                    modified = True
                else:
                    new_words.append(words[i])
            words = new_words
        return words



if __name__ == '__main__':
    print(Solution().removeAnagrams(["abba","baba","bbaa","cd","cd"]))