# Time: O(n) since we have to visit every node in the tree using recursion
# Space: O(log(n)) since the maximum amount of space needed corresponds to
# the depth of the balanced tree
#
# NOTE: Here's the definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Base case: Return None for a null root node
    if root == None:
      return None

    # Swap the root node's left and right children
    root.left, root.right = root.right, root.left

    # Recursively call the invertTree() method on the root node's children
    self.invertTree(root.left)
    self.invertTree(root.right)

    # Return the root node of the inverted binary tree
    return root