# Time: O(log(m*n)), where m and n are the rows and columns of the matrix,
# respectively, since we need to run binary search twice to find the given
# target element
# Space: O(1) since no extra memory is needed
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # Create variables to track the number of rows and columns in the matrix
    rows, columns = len(matrix), len(matrix[0])

    # Create pointers to track the first and last rows in the matrix
    first, last = 0, rows - 1

    # Check pointer bounds
    while first <= last:
      # Find the middle row
      middle = (first + last) // 2

      # Target is less than the first element in the middle row
      if target < matrix[middle][0]:
        last = middle - 1
      # Target is greater than the last element in the middle row
      elif target > matrix[middle][-1]:
        first = middle + 1
      else:
        # Target should be in the middle row
        break

    # Target doesn't exist in the matrix if the last pointer comes before first
    if last < first:
      return False

    # Create a variable to track the row where the target should be
    targetRow = (first + last) // 2

    # Create left and right pointers for the target row
    left, right = 0, columns - 1

    # Check pointer bounds
    while left <= right:
      # Find the middle element
      middle = (left + right) // 2

      # Target is less than the middle element
      if target < matrix[targetRow][middle]:
        right = middle - 1
      # Target is greater than the middle element
      elif target > matrix[targetRow][middle]:
        left = middle + 1
      # Target is the middle element
      else:
        return True

    # Target wasn't found in the row where it should be
    return False