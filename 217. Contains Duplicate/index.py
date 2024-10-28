from typing import List


class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
      collection = set()
      for each in nums: 
         if each in collection:
            return True
         else:
            collection.add(each)
            
      return False