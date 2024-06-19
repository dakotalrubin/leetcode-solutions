# Time: O(log(n)), since we need to run binary search on the input array once
# to find the pivot index and once again to find the target index
# Space: O(1) since no extra memory is needed
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # Create left and right pointers to maximize the search area
    left, right = 0, len(nums) - 1

    # Create a variable to store the first element from the input array
    firstElement = nums[0]

    # Find the pivot index
    while left < right:
      # Calculate the middle index
      middle = (left + right) // 2

      # If the middle element is greater than or equal to the first element,
      # search the right portion of the input array
      if nums[middle] >= firstElement:
        left = middle + 1
      # Else search the left portion of the input array
      else:
        right = middle - 1

    # After the while loop, the left pointer is the pivot index
    pivotIndex = left

    # Update left and right pointers: if target is greater than or equal to
    # the first element, search the left portion of the divided input array
    if target >= firstElement:
      left, right = 0, pivotIndex
    # Else search the right portion of the divided input array
    else:
      left, right = pivotIndex, len(nums) - 1

    # Find the target index
    while left <= right:
      # Calculate the middle index
      middle = (left + right) // 2

      # If the middle element is smaller than target, search the right portion
      if nums[middle] < target:
        left = middle + 1
      # Else if the middle element is greater than target, search the left portion
      elif nums[middle] > target:
        right = middle - 1
      # Else target is the middle element, so return the middle index
      else:
        return middle

    # Target doesn't exist in the input array
    return -1