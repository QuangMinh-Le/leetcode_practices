# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
   def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      res = []
      def treePaths(root, st): 
         if not root: 
            return
         st += str(root.val)
         if (not root.left and not root.right):
            res.append(st)
         treePaths(root.left, st + "->")
         treePaths(root.right, st + "->")
         return
      treePaths(root, "")
      return res