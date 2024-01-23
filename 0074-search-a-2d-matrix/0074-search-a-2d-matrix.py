# The solution has a time complexity of O(log(m * n)), where m and n are
# the rows and columns of the matrix, respectively. I use a consecutive
# binary search to find the given target element. The space complexity is
# O(1), since no extra data structures are needed.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Create two variables to track the number of rows and columns
        # in the matrix
        rows, columns = len(matrix), len(matrix[0])

        # Create two pointers to track the first and last rows in the matrix
        first, last = 0, rows - 1

        while first <= last:
            # Find the middle row
            middle = (first + last) // 2

            # If target is greater than the last element in the middle row
            if target > matrix[middle][-1]:
                first = middle + 1
            # If target is less than the first element in the middle row
            elif target < matrix[middle][0]:
                last = middle - 1
            else:
                break

        # Target doesn't exist in the matrix if the last row comes before the
        # first row we're considering
        if last < first:
            return False

        # Create a variable to track the row where target should be
        row = (first + last) // 2

        # Create left and right pointers
        left, right = 0, columns - 1

        while left <= right:
            # Find the middle element
            middle = (left + right) // 2

            # If target is greater than the middle element
            if target > matrix[row][middle]:
                left = middle + 1
            # If target is less than the middle element
            elif target < matrix[row][middle]:
                right = middle - 1
            # Target is the middle element
            else:
                return True

        # If target wasn't found in the row where it should be, return False
        return False