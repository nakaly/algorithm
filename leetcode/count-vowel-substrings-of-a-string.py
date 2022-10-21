
from itertools import permutations

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel = "aiueo"
        vowels = ["".join(list(i)) for i in permutations(vowel)]
        result = 0
        print(vowels)
        for vow in vowels:
            index = word.find(vow)
            if index >= 0:
                print(vow)
                result+=1
                i = 0
                while index+5+i < len(word) and word[index+5+i] in vowel:
                    result += 1
                    i += 1
        return result

# sliding window max
def find_maximum_in_sliding_window(window_size, arr):
    max_so_far = -sys.maxsize
    max_ending_here = -sys.maxsize
    start = 0
    end = 0
    while end < len(arr):
        max_ending_here = max(max_ending_here + arr[end], arr[end])
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if end - start + 1 == window_size:
            max_ending_here = max(max_ending_here - arr[start], arr[start])
            start += 1
        end += 1
    return max_so_far





if __name__ == '__main__':
    print(Solution().countVowelSubstrings("cuaieuouac"))