# The solution has a time complexity of O(n) since you need to iterate through
# the input array once using the two-pointer approach. The space complexity is
# O(1), since no extra memory is used.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Create a variable to track the maximum area
        maximum_area = 0

        # Create a left pointer and a right pointer
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the area of the current pointer elements (1-indexing)
            area = (right - left) * min(height[left], height[right])

            # Update the maximum area
            maximum_area = max(maximum_area, area)

            # Shift the pointer that points to the lower height
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            # If the pointers point to equal heights, just shift one of them
            else:
                left += 1

        return maximum_area