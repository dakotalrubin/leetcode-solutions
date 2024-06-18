# Time: O(log(n)) since we need to use binary search to divide the input array
# Space: O(1) since no extra memory is needed
class Solution:
  def findMin(self, nums: List[int]) -> int:
    # Create left and right pointers to initialize the search area
    left, right = 0, len(nums) - 1

    # Check pointer bounds
    while left < right:
      # Find the middle element
      middle = (left + right) // 2

      # Check if the middle element belongs to the left or right portion
      if nums[middle] > nums[right]:
        # Search the right portion of the array
        left = middle + 1
      else:
        # Search the left portion of the array
        right = middle

    # After the while loop, the left pointer will point to the minimum element
    return nums[left]