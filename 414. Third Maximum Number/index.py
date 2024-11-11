from typing import List


class Solution:
   def thirdMax(self, nums: List[int]) -> int:
      nums.sort(reverse=True)
      collection = []
      count = 0
      while len(collection) < 3 and count < len(nums):
         if nums[count] not in collection:
            collection.append(nums[count])
         count += 1
      if len(collection) < 3: 
         return max(nums)
      return collection[-1]