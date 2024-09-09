from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        res = []
        for x in nums:
            if x not in res:
                res.append(x)
                count += 1
        # Modify the original nums list in-place
        nums[:] = res  # Use slice assignment to modify the original list
        return count