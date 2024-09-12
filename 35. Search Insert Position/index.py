from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        while count < len(nums):
            if nums[count] < target:
               count += 1
               continue
            elif nums[count] >= target:
               break
            count += 1
        
        return count