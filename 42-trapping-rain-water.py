# Time: O(n) since you need to iterate through the input array once using
# the two-pointer approach
# Space: O(1) since no extra memory is needed
class Solution:
  def trap(self, height: List[int]) -> int:
    # Create a variable to store the total trapped units of water
    total = 0

    # Create left and right pointers
    left, right = 0, len(height) - 1

    # Create variables to track the maximum left and right heights seen
    maxLeft, maxRight = 0, 0

    # Check pointer bounds
    while left < right:
      # Update the maximum left and right heights seen
      maxLeft, maxRight = max(maxLeft, height[left]), max(maxRight, height[right])

      # The left side of the container is shorter than the right side
      if maxLeft < maxRight:
        # Calculate the water trapped at the left pointer element
        water = min(maxLeft, maxRight) - height[left]
        left += 1
      # The right side of the container is shorter than or equal to the left side
      else:
        # Calculate the water trapped at the right pointer element
        water = min(maxLeft, maxRight) - height[right]
        right -= 1

      # Only add positive amounts of water to the total
      if water > 0:
        total += water

    return total