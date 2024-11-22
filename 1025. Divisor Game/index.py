import math
class Solution:
   def divisorGame(self, n: int) -> bool:
      Alice = False
      while n > 1:
         n = n - 1
         Alice = not Alice
      return Alice