# Time: O(n) since you need to iterate through the input array once using
# the two-pointer approach
# Space: O(1) since no extra memory is needed
class Solution:
  def maxArea(self, height: List[int]) -> int:
    # Create a variable to track the maximum area
    maximumArea = 0

    # Create left and right pointers that maximize the initial area
    left, right = 0, len(height) - 1

    # Check pointer bounds
    while left < right:
      # Calculate the area formed by the current pointer elements (a rectangle)
      currentArea = (right - left) * min(height[left], height[right])

      # Update the maximum area
      maximumArea = max(maximumArea, currentArea)

      # Shift the pointer that points to the lower height
      if height[left] < height[right]:
        left += 1
      elif height[right] < height[left]:
        right -= 1
      else:
        # If both pointers point to equal heights, just shift one of them
        left += 1

    return maximumArea