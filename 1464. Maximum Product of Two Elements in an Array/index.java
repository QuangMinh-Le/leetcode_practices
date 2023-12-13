class Solution {
   public int maxProduct(int[] nums) {
      int res = 0; 

      if (nums.length == 2) {
         res = (nums[0] - 1)*(nums[1] - 1);
      } else {
         int max1 = nums[0];
         int max2 = nums[1];
         int count = 2;

         while (count < nums.length) {
            if (nums[count] >= max1 ) {
               if (max1 >= max2) {
                  max2 = max1;
               }
               max1 = nums[count];
            } else if (nums[count] >= max2) {
               max2 = nums[count];
            }
            count ++;
         }
         res = (max1 - 1)*(max2 - 1);
      }
      return res;
   }
}