# Time: O(n*log(m)), where n is the length of the input array and m is the
# maximum value in the input array; taking the maximum value is O(n), and then
# we perform binary search on an array of potential k values for each element
# in the input array, which results in O(n*log(m))
# Space: O(1) since no extra memory is needed

import math

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # Set the left pointer as the smallest possible eating speed, and set the
    # right pointer as the maximum value in the input array
    left, right = 1, max(piles)

    # Create a variable to track the minimum eating speed (k)
    # Initialize k == max(piles) since this is the worst-case solution
    k = right

    # Check pointer bounds
    while left <= right:
      # Find the middle element in the array of potential k values
      middle = (left + right) // 2

      # Create a variable to track the total hours needed to eat all piles
      hours = 0

      # Add the hours needed to eat each pile
      for pile in piles:
        hours += math.ceil(pile / middle)

      # If we needed less hours than the maximum hours given (h)
      if hours <= h:
        # The new minimum eating speed is the middle element in the current
        # range of potential k values
        k = middle

        # Try to look for a smaller k value
        right = middle - 1

      else:
        # We took too many hours, so try to look for a larger k value
        left = middle + 1

    # Return the minimum eating speed (k)
    return k