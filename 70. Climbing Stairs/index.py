class Solution:
   def climbStairs(self, n: int) -> int:
      res = 0
      base_1_step_before = 2
      base_2_step_before = 1
      if n == 1:
         res = 1
      elif n == 2:
         res = 2
      else:
         c = 3
         while c <= n:
            res = base_1_step_before + base_2_step_before
            base_2_step_before = base_1_step_before
            base_1_step_before = res
            c += 1
      return res