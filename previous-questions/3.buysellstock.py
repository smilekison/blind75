class Solution:
    def maxProfit(prices: list[int]) -> int:  # Method to calculate the maximum profit from stock prices
        min_price = float("inf")
        maxP = 0


        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > maxP:
                maxP = price - min_price
        return maxP