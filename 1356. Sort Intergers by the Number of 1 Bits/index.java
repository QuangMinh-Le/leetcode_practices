import java.util.Arrays;

class Solution {
   public int[] sortByBits(int[] arr) {
      int size = arr.length;

      int[] res = new int[size];

      for (int i = 0; i < arr.length; i++) {
         int temp = 100000;
         String bString = Integer.toBinaryString(arr[i]);
         int cnt = (int) bString.chars().filter(ch -> ch == '1').count();
         
         temp = (temp * cnt) + arr[i];
         res[i] = temp;

      }
      Arrays.sort(res);
      for (int j = 0; j < res.length; j++) {
         res[j] = res[j] % 100000;
      }
      
      return res;     
   }
}