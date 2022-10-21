

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        num_of_w = 0
        result = 1000
        block_length = len(blocks)
        for i in range(block_length):
            if blocks[i] == 'W':
                num_of_w += 1
            if i >= k-1:
                result = min(result, num_of_w)
            if i-k+1 >= 0 and blocks[i-k+1] == 'W':
                num_of_w -= 1
        return result


if __name__ == '__main__':
    print(Solution().minimumRecolors("BWWWBB", 6))