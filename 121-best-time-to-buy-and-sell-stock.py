# Time: O(n) since you need to iterate through the input array once using
# the sliding window approach with two pointers
# Space: O(n) since no extra memory is needed
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # Left and right pointers represent minimum price and current price
    left, right = 0, 1

    # Create a variable to track the maximum profit
    maxProfit = 0

    # Check pointer bounds
    while right < len(prices):
      # If the minimum price is less than the current price
      if prices[left] < prices[right]:
        # Calculate the profit and update the maximum profit
        profit = prices[right] - prices[left]
        maxProfit = max(maxProfit, profit)
      else:
        # The new minimum price is the current price
        left = right

      # Increment the right pointer to check a new price
      right += 1

    return maxProfit