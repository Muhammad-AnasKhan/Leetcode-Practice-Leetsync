class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff =  prices[j] - prices[i]
        #         max_profit = max(diff, max_profit)

        # return max_profit

        # Using One Pass
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            # min_price = min(min_price, prices[i])
            # max_profit = max(max_profit, prices[i] - min_price)
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit