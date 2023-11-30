import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode() {}
   TreeNode(int val) { this.val = val; }
   TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
   }
}


class Solution {
   public int averageOfSubtree(TreeNode root) {
      int counter = 0;
      int sum = 0;
      int res = 0;
      while (root != null) {
         inOrderTraversal(sum, counter, root);
         if (sum/counter == root.val) res ++;
         
         if (root.left != null) {
            root = root.left;
         } else if (root.right != null) {
            root = root.right;
         }
      }
      return res;
   }
   private void inOrderTraversal(int sum, int counter, TreeNode node) {
      if (node == null) {
         return;
      }
      else {
         counter ++;
         sum += node.val;
         if (node.left != null) {
            inOrderTraversal(sum, counter, node.left);
         }
         if (node.right != null) {
            inOrderTraversal(sum, counter, node.right);
         }
      }

   }
}