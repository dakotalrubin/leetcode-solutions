# Solution is O(m * nlog(n)), where O(m) is the time complexity of
# iterating through the entire input array strs, and O(nlog(n)) is
# the time complexity of using a comparison-based sort on each
# element in the input array strs.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where each key is a sorted string
        # from strs, and each value is a list of anagrams
        anagram_dict = defaultdict(list)

        for str in strs:
            # Create a list of each alphabetically-sorted string in strs
            sorted_str = sorted(str)

            # Create a key string for the dictionary from each list
            key_str = ''.join(sorted_str)

            # Add the original str to the dictionary at the right key
            anagram_dict[key_str].append(str)

        # Return a list of grouped anagrams
        return list(anagram_dict.values())