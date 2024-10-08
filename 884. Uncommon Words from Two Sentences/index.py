from typing import List
from collections import Counter 

class Solution:
   def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      temp = s1 + " " + s2
      arr = temp.split()
      res = []
      checker = Counter(arr)
      for key, value in checker.items():
         if value == 1: 
            res.append(key)
      
      return res
      
      