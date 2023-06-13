class Solution {
    public int removeElement(int[] nums, int val) {
        int length = nums.length;
        int counter = 0;
        int count = 0;

        int res_arr_count = 0;
        for (int i = 0; i < length; i++) {
            if (nums[i] != val) {
                counter ++;
            };
        };
        int res_arr[] = new int[counter];

        for (int i = 0; i < length; i++) {
            if (nums[i] != val) {
                res_arr [count] = nums[i];
                count ++;
            };
        };
        for (int j = 0; j < res_arr.length; j++) {
            nums [j] = res_arr[j];
        };
        return counter;
         
        
    };
}