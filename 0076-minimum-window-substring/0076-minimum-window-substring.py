# The solution has a time complexity of O(m+n), where the input strings
# s and t have lengths m and n, respectively. There is a linear time
# solution using the sliding window approach with two pointers. The
# space complexity is constant, since each of the two hashmaps needed
# will have at most 52 entries, because only uppercase and lowercase
# English characters are involved.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create a variable that contains the minimum valid substring
        # and another that contains its length (default: infinity)
        min_substring = ""
        min_substring_length = float("infinity")

        # Cover the cases where string t is an empty string or longer
        # than string s
        if t == "" or len(t) > len(s):
            return min_substring

        # tCount stores char-frequency pairs for string t, and window
        # stores char-frequency pairs for string s (in the current window)
        tCount, window = {}, {}

        # Store every char and its frequency from string t in tCount
        for char in t:
            if char in tCount:
                tCount[char] += 1
            else:
                tCount[char] = 1

        # "have" is the number of chars in the current window that also
        # belong to tCount in the proper quantity, and "need" is 
        # the length of tCount
        have, need = 0, len(tCount)

        # Create left and right pointers for the sliding window
        left = right = 0

        while right < len(s):
            # Add the rightmost char in the current window to the 
            # window hashmap
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            # Increment "have" if the rightmost char also belongs
            # to tCount in the exact same quantity
            if s[right] in tCount and window[s[right]] == tCount[s[right]]:
                have += 1

            while have == need:
                # Update the minimum valid substring and its length
                if (right - left + 1) < min_substring_length:
                    min_substring = s[left:(right + 1)]
                    min_substring_length = len(min_substring)

                # Decrement the quantity of the leftmost char from the
                # current window
                window[s[left]] -= 1

                # Decrement "have" if the leftmost char also belongs
                # to tCount in a different quantity
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1

                # Increment the left pointer to decrease the window size
                left += 1

            # Increment the right pointer to increase the window size
            right += 1

        return min_substring