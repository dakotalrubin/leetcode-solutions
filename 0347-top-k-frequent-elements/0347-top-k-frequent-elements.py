# The solution has a time complexity of O(n) and a space complexity of O(n)
# using bucket sort, which is a non-comparison-based sorting algorithm.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to count the frequency of each element
        # in the input array
        count_dict = {}

        # Add each element from the input array to count_dict: each
        # key is an element from the input array, and each value
        # is its frequency
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        # Create an array that contains a number of empty lists
        # equal to the size of the input array
        buckets = [[] for i in range(len(nums) + 1)]

        # Each "num" occurs "frequency" times: "frequency" is the index
        # of "num" in the buckets array
        for num, frequency in count_dict.items():
            buckets[frequency].append(num)

        # Create a list that contains the top k most-frequent elements
        top_freq = []

        # Retrieve k elements from the buckets array starting from the end
        for i in range(len(buckets) - 1, 0, -1):
            for element in buckets[i]:
                top_freq.append(element)

            # Stop when top_freq contains k elements
            if len(top_freq) == k:
                return top_freq
