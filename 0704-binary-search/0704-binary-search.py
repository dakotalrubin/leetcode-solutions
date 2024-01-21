# The solution has a time complexity of O(log(n)), since the input array
# is already sorted and we use the binary search algorithm to find the 
# target value. The space complexity is O(1), since no extra data
# structures are needed.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Create left and right pointers
        left, right = 0, len(nums) - 1

        while left <= right:
            # Create a middle pointer to bisect the search area
            middle = (left + right) // 2

            # Target is in the right half of the input array
            if target > nums[middle]:
                left = middle + 1
            # Target is in the left half of the input array
            elif target < nums[middle]:
                right = middle - 1
            # Target's index is the middle element of the input array
            else:
                return middle

        # Target doesn't exist in the input array
        return -1