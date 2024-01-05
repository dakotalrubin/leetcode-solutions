# The solution has a time complexity of O(n), since you have to iterate
# through the input string once using two pointers, and a space complexity
# of O(1) because no extra memory is used.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Set pointers to the first and last chars in string s
        left = 0
        right = len(s) - 1

        # Loop until left pointer meets right pointer
        while left < right:
            # Skip past non-alphanumeric left pointer chars
            if not self.isAlNum(s[left]):
                left += 1
            # Skip past non-alphanumeric right pointer chars
            elif not self.isAlNum(s[right]):
                right -= 1
            # Compare lowercase alphanumeric chars
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        # String s is a valid palindrome
        return True

    # Helper function checks whether a given ASCII char is alphanumeric
    def isAlNum(self, c: chr) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))