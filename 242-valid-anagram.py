# Time: O(n) because you need to iterate over each string once
# Space: O(n) because you need to create a hashmap, which might need to
# store every letter in the first string as a unique letter
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # Compare string lengths: if unequal, the strings aren't anagrams
    if len(s) != len(t):
      return False

    # Create a hashmap, where keys are characters and values are their counts
    countS = {}

    # Iterate through string s and add its characters and counts to the hashmap
    for i in range(len(s)):
      if s[i] in countS:
        countS[s[i]] += 1
      else:
        countS[s[i]] = 1

    # Iterate through string t and subtract its characters and counts
    # from the hashmap
    for i in range(len(t)):
      if t[i] in countS:
        countS[t[i]] -= 1
      else:
        # This character isn't part of string s, so the strings aren't anagrams
        return False

    # Check to make sure the hashmap character counts are all zero
    for i in range(len(s)):
      if countS[s[i]] != 0:
        return False

    # The strings are anagrams
    return True