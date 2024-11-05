from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
         res = []
         for each in nums1: 
            if each == max(nums2):
               res.append(-1)
            else:
               temp = nums2.index(each)
               status = True
               for i in range(temp, len(nums2)):
                  if nums2[i] > each:
                     res.append(nums2[i])
                     status = False
                     break
               if status: 
                  res.append(-1)   
         return res
                  
               