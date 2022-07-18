from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        answer = []
        first_match = False
        tokens = text.split()
        index = 0
        num_of_tokens = len(tokens)
        while index < num_of_tokens:
            print("word", tokens[index])
            if not first_match:
                first_match = tokens[index] == first
            else:
                if tokens[index] == second:
                    if index < num_of_tokens:
                        answer.append(tokens[index+1])
                first_match = False
            index += 1
        return answer


if __name__ == '__main__':
    print(Solution().findOcurrences("we will we will rock you", "we", "will"))