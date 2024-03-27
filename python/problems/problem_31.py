from typing import List


class Problem31:
    TITLE = "Coin Sums"
    DESCRIPTION = "https://projecteuler.net/problem=31"

    def get_number_of_ways(self, coins_sum: int, coins: List[int]) -> int:
        ways = [0 for _ in range(coins_sum + 1)]
        ways[0] = 1

        for coin in coins:
            for j in range(len(ways)):
                if coin <= j:
                    ways[j] += ways[j - coin]

        return ways[coins_sum]

    def answer(self) -> int:
        coins = [1, 2, 5, 10, 20, 50, 1_00, 2_00]

        return self.get_number_of_ways(200, coins)
