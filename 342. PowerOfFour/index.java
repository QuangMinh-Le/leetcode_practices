// class Solution {
//    public boolean isPowerOfFour(int n) {
//       if (n == 0) {
//          return false;
//       }
//       else {
//          int temp = 0;

//          while (temp == 0) {
//             n = n / 4;
//             temp = n % 1;
//          }
//          if (n == 1) {
//             return true;
//          } else {
//             return false;
//          }
//       }
//    }
// }

class Solution {
   public boolean isPowerOfFour(int n) {
      int check = n % 4;
      if (n == 0) {
         return false;
      } else if (check > 0) {
         return false;
      }
      else {
         int temp = 1;
         if (n > 1048576) {
            n = n/1048576;
         } 
         while (temp < n) {
            temp = temp * 4;
         }
         if (temp == n) {
            return true;
         } else {
            return false;
         }
      }
   }
}