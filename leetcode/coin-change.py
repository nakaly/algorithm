
import math
from typing import List
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()
        coins.reverse()
        minimum = [sys.maxsize]
        # print(coins)
        if amount == 0:
            return 0
        result = self.coinChangeRec(coins, amount, 0, memo, minimum)
        if result == sys.maxsize:
            return - 1
        return result


    def coinChangeRec(self, sorted_coins: List[int], amount: int, num_of_coins: int, memo: dict, minimum: int) -> int:
        print("maji start: sorted_coins: ", sorted_coins, " amount: ", amount, " num_of_coins: ", num_of_coins, " minimum", minimum)
        if num_of_coins > minimum[0]:
            return minimum[0]
        if amount in memo:
            # print("in memo", amount)
            return memo[amount] + num_of_coins
        max_coin = 0

        max_coin_index = -1
        for i, coin in enumerate(sorted_coins):
            if coin <= amount:
                max_coin = coin
                max_coin_index = i
                break
        print("start: sorted_coins: ", sorted_coins, " amount: ", amount, " num_of_coins: ", num_of_coins, " minimum", minimum, "max_coin", max_coin, " max_coin_index", max_coin_index)
        if max_coin == 0:
            memo[amount] = sys.maxsize
            return sys.maxsize
        max_usage_of_max_coin = math.floor(amount / coin)

        print("max_usage_of_max_coin", max_usage_of_max_coin)
        next_amount = amount % max_coin
        print("next_amount", next_amount)
        if next_amount != 0 and max_usage_of_max_coin == 0:
            memo[amount] = sys.maxsize
            return sys.maxsize
        if next_amount == 0:
            answer = num_of_coins + max_usage_of_max_coin
            # print("success: sorted_coins: ", sorted_coins, " amount: ", amount, " num_of_coins: ", num_of_coins)
            # print("success!!!", answer)
            # print("minimum", minimum)
            memo[str(amount) + "_".join(map(str, sorted_coins))] = answer
            minimum[0] = min(minimum[0], answer)
            return max_usage_of_max_coin + num_of_coins
        result = sys.maxsize
        for usage_of_max_coin in range(max_usage_of_max_coin, -1, -1):
            print("usage_of_max_coin", usage_of_max_coin)
            next_amount = amount - max_coin * usage_of_max_coin
            next_num_of_coin = num_of_coins + usage_of_max_coin
            # print("next_num_of_coin", next_num_of_coin)
            if next_num_of_coin > minimum[0]:
                new_result = minimum[0]
            else:
                # print("next_num_of_coin2", next_num_of_coin)
                new_result = self.coinChangeRec(sorted_coins, next_amount, next_num_of_coin, memo, minimum)
                # print("new_result", new_result)
            result = min(result, new_result)
            # print("result", result)
            minimum[0] = min(minimum[0], result)

        return result


if __name__ == '__main__':
    print(Solution().coinChange([411,412,413,414,415,416,417,418,419,420,421,422], 9864))