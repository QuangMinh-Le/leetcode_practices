from typing import List


class Solution:
   def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      res = set()
      for each in nums1: 
         if each in nums2: 
            res.add(each)
            
      return list(res)