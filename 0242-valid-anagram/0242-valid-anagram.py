# Solution takes O(n) + O(n) + O(n) = O(3n) => O(n) time complexity
# and O(n) space complexity because only one dictionary is needed
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If strings aren't equal length, they can't be anagrams
        if len(s) != len(t):
            return False

        # Create a dictionary for the first string, where letters
        # are keys and the letter counts are values
        anagram_dict = {}

        # Add each letter of the first string to the dictionary
        # or increment the pre-existing letter count
        for letter in s:
            if letter in anagram_dict.keys():
                anagram_dict[letter] += 1
            else:
                anagram_dict[letter] = 1

        # Check whether each letter in the second string appears
        # in the dictionary, and if so, decrement the letter count
        for letter in t:
            if letter in anagram_dict.keys():
                anagram_dict[letter] -= 1
            # If the letter in the second string doesn't exist
            # in the dictionary, the two strings aren't anagrams
            else:
                return False

        # If each value in the dictionary isn't zero, the two
        # strings can't be anagrams
        for value in anagram_dict.values():
            if value != 0:
                return False

        # The two strings must be anagrams
        return True