# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dig(root: Optional[TreeNode]):
           if not root:
              return 0
           left_depth = dig(root.left)
           right_depth = dig(root.right)
           
           return max(left_depth, right_depth) + 1
        
        return dig(root)