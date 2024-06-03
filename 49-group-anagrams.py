# Time: O(m*nlog(n)), where m is the length of the input array and n is the
# average length of each string in the input array
# NOTE: O(nlog(n)) is the time complexity of using a comparison-based sort on
# each string in the input array
# Space: O(n) because you need to create a hashmap, which might need to store
# every string in the input array as a unique entry
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Create a hashmap, where each key is a sorted string from the input
    # array and each value is a list of grouped anagrams
    anagrams = defaultdict(list)

    for string in strs:
      # Create a sorted list of characters from the current string
      sortedString = sorted(string)

      # Create a key for the hashmap from each sorted list of characters
      key = ''.join(sortedString)

      # Append the current string to the list of grouped anagrams at the
      # proper key
      anagrams[key].append(string)

    # Return a list of grouped anagram lists (A.K.A. all values in the hashmap)
    return list(anagrams.values())