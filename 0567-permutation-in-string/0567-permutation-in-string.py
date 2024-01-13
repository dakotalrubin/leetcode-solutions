# The solution has a time complexity of O(n) using the sliding window
# approach to iterate through string s2. Since only lowercase English
# chars are used, the hashmaps for both strings can be compared in
# constant time. The space complexity is constant, since two hashmaps
# are needed, but the size of each will be capped at 26 entries max.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check whether string s2 contains enough chars to support
        # a permutation of string s1
        if len(s1) > len(s2):
            return False

        # s1Count stores char-frequency pairs for string s1, and s2Count
        # stores char-frequency pairs for string s2 (in the current window)
        s1Count = {}
        s2Count = {}

        # Store every char and its frequency from string s1 into s1Count
        for char in s1:
            if char in s1Count:
                s1Count[char] += 1
            else:
                s1Count[char] = 1

        # Create left and right pointers for the sliding window
        # The size of the sliding window will always be the size of s1
        left, right = 0, len(s1) - 1

        # Add the chars in the first window to s2Count
        for i in range(len(s1)):
            if s2[i] in s2Count:
                s2Count[s2[i]] += 1
            else:
                s2Count[s2[i]] = 1

        while right < len(s2):
            # Check whether s2 contains a permutation of s1
            if s1Count == s2Count:
                return True

            # Remove the leftmost char in the current window from s2Count
            s2Count[s2[left]] -= 1
            if s2Count[s2[left]] == 0:
                s2Count.pop(s2[left])

            # Shift the window
            left += 1
            right += 1

            # Add the rightmost char in the new window to s2Count
            if right < len(s2):
                if s2[right] in s2Count:
                    s2Count[s2[right]] += 1
                else:
                    s2Count[s2[right]] = 1

        return False
