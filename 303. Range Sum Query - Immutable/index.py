from typing import List


class NumArray:

   def __init__(self, nums: List[int]):
      self.numArray = nums
   def sumRange(self, left: int, right: int) -> int:
      res = 0
      for i in range(left, right):
         res += self.numArray[i]
      return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)