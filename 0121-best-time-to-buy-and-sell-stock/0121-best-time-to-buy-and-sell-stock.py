# The solution has a time complexity of O(n), since you need to iterate
# through the input array once using the sliding window approach with two
# pointers. The space complexity is O(1), since no extra memory is used.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Create a variable to track the max profit seen so far
        max_profit = 0

        # Check to make sure there's more than one day of price data
        if len(prices) > 1:
            # Create a left pointer to track the best day to buy
            # and a right pointer to track the best day to sell
            left, right = 0, 1

            while right < len(prices):
                # Calculate the current profit
                current_profit = prices[right] - prices[left]

                # If you don't make a profit, try new days to buy and sell
                if current_profit < 0:
                    left = right # Update the minimum price
                    right += 1
                # Update the max profit and try a new day to sell
                else:
                    max_profit = max(max_profit, current_profit)
                    right += 1

        return max_profit