class Solution:
   def addDigits(self, num: int) -> int:
      if num < 10: 
         return num
      if num % 9 == 0:
         return 1 + (num - 1) % 9
      else: 
         return num % 9