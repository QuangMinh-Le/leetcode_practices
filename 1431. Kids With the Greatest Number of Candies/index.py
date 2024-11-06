from typing import List


class Solution:
   def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      # Kid with greatest candies before extra candies
      bef_max = max(candies)
      res = []
      for each in candies:
         if each + extraCandies >= bef_max:
            res.append(True)
         else: 
            res.append(False)
              
      return res