class Solution {
    public int numSpecial(int[][] mat) {
      int res = 0;
      
      for (int index = 0; index < mat.length; index++) {
         int checker_row = 0;
         int position_1 = -1;
         for (int i = 0; i < mat[0].length; i++) {
            checker_row += mat[index][i];
            if (mat[index][i] == 1) {
               position_1 = i;
            }
         }
         if (checker_row == 1) {
            int checker = 0;
            for (int i = 0; i < mat.length; i++) {
               checker += mat[i][position_1];
            }
            if (checker == 1) {
               res ++;
            }
            
         }
      }
      return res;
    }
}