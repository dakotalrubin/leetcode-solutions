# Time: O(log(n)) because the input array is already sorted and every iteration
# of binary search reduces the problem size by half
# Space: O(1) because no extra data structures are needed
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # Create left and right pointers
    left, right = 0, len(nums) - 1

    while left <= right:
      # Create a middle pointer to bisect the search area
      middle = (left + right) // 2

      if target > nums[middle]:
        # Target is in the right half of the search area
        left = middle + 1
      elif target < nums[middle]:
        # Target is in the left half of the search area
        right = middle - 1
      else:
        # Target is the middle element of the search area
        return middle

    # Target doesn't exist in the search area
    return -1