class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
      pointer1 = 0
      pointer2 = 0
      while pointer2 < len(t) and pointer1 < len(s):
         if s[pointer1] == t[pointer2]:
            pointer1 += 1
         pointer2 += 1
         
      return pointer1 == len(s)