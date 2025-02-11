class Solution:
    def maxProfit(prices: list[int]) -> int:  # Method to calculate the maximum profit from stock prices
        min_price = float('inf')  # Initialize min_price to infinity to track the lowest price seen so far
        max_profit = 0  # Initialize max_profit to 0 to track the maximum profit achievable

        for price in prices:  # Iterate through each price in the list
            if price < min_price:  # If the current price is lower than min_price, update min_price
                min_price = price
            elif price - min_price > max_profit:  # If selling at the current price yields a higher profit, update max_profit
                max_profit = price - min_price

        return max_profit  # Return the maximum profit found

    print(maxProfit([7,1,5,7,4]))  # Test the function with an example


'''
Summary

    DSA Used: Greedy Algorithm on a list of prices.

    Time Complexity: O(n).

    Space Complexity: O(1).

'''