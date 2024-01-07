# The solution has a time complexity of O(nlog(n)) for sorting the input array
# plus O(n^2) for using a nested loop (iterating through the input array,
# then checking number combinations with the two-pointer approach), yielding
# an overall time complexity of O(n^2). The space complexity is O(n) using
# Python's sort() method.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Create a list of unique triplets
        triplets = []

        # Sort the input array
        nums.sort()

        # "a" is the first element in a triplet
        for i, a in enumerate(nums):

            # Skip duplicate elements for "a"
            if i > 0 and a == nums[i - 1]:
                continue

            # Create left and right pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                # Calculate the sum of the current pointer elements
                sum = a + nums[left] + nums[right]

                # If the sum is greater than zero, decrement right pointer
                if sum > 0:
                    right -= 1
                # If the sum is less than zero, increment left pointer
                elif sum < 0:
                    left += 1
                # The sum equals zero, so add the triplet to the solution
                else:
                    triplets.append([a, nums[left], nums[right]])

                    # Continue through the input array for more unique triplets
                    left += 1

                    # Skip duplicate elements for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets