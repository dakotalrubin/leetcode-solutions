# The solution has a time complexity of O(n), since you need to iterate
# through the input array once using the two-pointer approach. The space
# complexity is O(1), since no extra memory is used.
class Solution:
    def trap(self, height: List[int]) -> int:
        # Create a variable to store the trapped units of water
        total = 0

        # Create left and right pointers
        left, right = 0, len(height) - 1

        # Create variables to track the max left and right pointer elements
        # seen so far
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft > maxRight:
                # If maxLeft is taller, decrement the right pointer
                right -= 1

                # Update the max right pointer element seen so far
                maxRight = max(maxRight, height[right])

                # Calculate the amount of water that can be trapped here
                water = min(maxLeft, maxRight) - height[right]

            else:
                # Else if maxRight is taller or equal to maxLeft, increment
                # the left pointer
                left += 1

                # Update the max left pointer element seen so far
                maxLeft = max(maxLeft, height[left])

                # Calculate the amount of water that can be trapped here
                water = min(maxLeft, maxRight) - height[left]

            # Only add positive amounts of water to the total
            if water > 0:
                total += water

        return total