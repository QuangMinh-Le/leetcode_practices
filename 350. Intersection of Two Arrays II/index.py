from typing import List


class Solution:
   def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      res = []
      
      less_nums = min(nums1, nums2)
      more_nums = max(nums1, nums2)
      
      while len(less_nums) >= 1: 
         if len(less_nums) ==1: 
            if less_nums[0] in more_nums:
               res.append(less_nums[0])
            return res
         each = less_nums[0]
         if each in more_nums: 
            res.append(each)
            more_nums.remove(each)
         less_nums.remove(each)
      return res