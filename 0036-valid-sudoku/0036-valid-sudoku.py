# The solution has a constant time complexity (bounded by the size of
# the board) for the use of O(1) hash map inserts and O(1) hash map
# lookups. The space complexity is constant size too, because it's necessary
# to create three hash maps to store all elements in the board.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create three hash maps: one for checking all rows, one for
        # checking all columns, and one for checking each 3x3 subgrid
        rows = defaultdict(set) # Key: board row (0-8)
        columns = defaultdict(set) # Key: board column (0-8)
        subgrids = defaultdict(set) # Key: (subgrid row (0-2), subgrid column (0-2))

        # Iterate through the board
        for row in range(9):
            for column in range(9):
                # Ignore empty cells
                if board[row][column] == ".":
                    continue

                # Check rows, columns and subgrids for duplicates
                if (board[row][column] in rows[row] or
                   board[row][column] in columns[column] or
                   board[row][column] in subgrids[(row // 3, column // 3)]):
                    return False

                # Add unique elements to the hash maps
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                subgrids[(row // 3, column // 3)].add(board[row][column])

        # The board is valid and contains no duplicates
        return True