from typing import List


class Solution:
   def arrayRankTransform(self, arr: List[int]) -> List[int]:
      temp_sorted = sorted(set(arr))
      
      rank = {val: i + 1 for i, val in enumerate(temp_sorted)}
      return [rank[val] for val in arr]