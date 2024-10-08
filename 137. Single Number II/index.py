from typing import List


class Solution:
   def singleNumber(self, nums: List[int]) -> int:
      if len(nums) == 1:
          return nums[0]
      
      nums.sort()
      
      for i in range(0, len(nums) - 1, 3):
          if i == len(nums) - 1 or nums[i] != nums[i+1]:
              return nums[i]
      
      return nums[-1]