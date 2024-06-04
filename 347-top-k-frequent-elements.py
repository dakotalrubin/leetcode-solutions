# Time: O(n) using bucket sort, which is a non-comparison-based sorting algorithm
# Space: O(n) because you need to create a hashmap to count the frequency of each
# element in the input array, and you need to create an array to store the
# results of performing bucket sort
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Create a hashmap to count the frequency of each element in the input array
    count = {}

    for num in nums:
      # Add each element from the input array to the hashmap: each key is an
      # element from the input array and each value is its frequency
      if num in count:
        count[num] += 1
      else:
        count[num] = 1

    # Create an array that contains a number of empty lists (buckets) equal
    # to the size of the input array + 1
    buckets = [[] for i in range(len(nums) + 1)]

    # Iterate through the keys and values in the count hashmap
    for num, frequency in count.items():
      # "frequency" becomes the index of "num" in the buckets array
      buckets[frequency].append(num)

    # Create an array that contains the top k most frequent elements
    topFreq = []

    # range(start, stop, step)
    for i in range(len(buckets) - 1, 0, -1):
      # Retrieve elements from the buckets array starting from the end
      for element in buckets[i]:
        topFreq.append(element)

      # Stop when topFreq contains k elements
      if len(topFreq) == k:
        return topFreq