
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
         boolean res = false;
         String left;
         String right;
         for ( int i = 0; i < word1.length; i++) {
            left = left + word1[i]
         }
         for (int j = 0; j < word2.length; j++) {
            right = right + word2[j];
         }
         res = left.equals(right);
         return res;
    }
}
