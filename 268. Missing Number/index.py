from typing import List


class Solution:
   def missingNumber(self, nums: List[int]) -> int:
      faster_checker = set(nums)
      lim = len(nums) + 1
      
      for i in range(0, lim):
         if i not in faster_checker: 
            return i