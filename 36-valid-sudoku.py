# Time: O(9*9) because the time complexity is bounded by the size of the board
# Space: O(9*9) because three hashmaps are needed to store all board elements
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Create three hashmaps for checking rows, columns and 3x3 subgrids
    rows = defaultdict(set) # Key: row number (0-8)
    columns = defaultdict(set) # Key: column number (0-8)
    subgrids = defaultdict(set) # Key: (subgrid row (0-2), subgrid column (0-2))

    # Iterate through the entire board
    for row in range(9):
      for column in range(9):
        # Ignore empty cells
        if board[row][column] == ".":
          continue

        # Check rows, columns and subgrids hashmaps for duplicates
        if (board[row][column] in rows[row]
          or board[row][column] in columns[column]
          or board[row][column] in subgrids[(row // 3, column // 3)]):
          return False

        # Add unseen elements to all three hashmaps
        rows[row].add(board[row][column])
        columns[column].add(board[row][column])
        subgrids[(row // 3, column // 3)].add(board[row][column])

    # The current state of the board is valid and contains no duplicates
    return True