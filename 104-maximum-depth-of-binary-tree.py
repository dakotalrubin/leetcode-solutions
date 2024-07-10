# Time: O(n) since we need to traverse every node in the tree using the recursive
# depth-first search approach to calculate the tree's height
# Space: O(n) since we need an amount of memory equal to the height of the tree
#
# Here's the definition for a binary tree node:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Base case for recursion: check whether the root node of the tree is null
    if not root:
      return 0

    # Run a recursive depth-first search approach and choose the maximum height
    # between the left and right subtrees, then add 1 for the root node height
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))