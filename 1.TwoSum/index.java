class Solution {
   public int[] twoSum(int[] nums, int target) {
      int x = -1;
      int y = -1;
      int [] res = new int[2];
      for (int i = 0; i < nums.length - 1; i++) {
         for (int j = i + 1; j < nums.length; j++) {
            int check = nums[i] + nums[j];
            if (target == check) {
               x = i;
               y = j;
            }
         }
      }
      res[0] = x;
      res[1] = y;
      return res;
   }
}