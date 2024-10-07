class Solution:
   def minLength(self, s: str) -> int:
      stat = True
      
      while stat:
         s = s.replace("AB", "")
         s = s.replace("CD", "")
         if "AB" not in s and "CD" not in s: 
            stat = False
      
      return len(s)
         