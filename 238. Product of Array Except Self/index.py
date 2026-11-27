from typing import List


class Solution:
   def productExceptSelf(self, nums: List[int]) -> List[int]:
      prod = 1
      collection = []
      count_zero = 0
      for each in nums: 
         if each != 0:
            prod = prod * each
         if each == 0: 
            count_zero += 1
      if count_zero == 1:
         for each in nums: 
            if each == 0: 
               collection.append(prod)
            else:  
               collection.append(0)
      if count_zero > 1: 
         for each in nums: 
            collection.append(0)
      if count_zero == 0:
         for each in nums: 
            collection.append(int(prod/each)) 
         
      return collection