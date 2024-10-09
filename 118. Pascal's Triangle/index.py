from typing import List


class Solution:
   def generate(self, numRows: int) -> List[List[int]]:
      res = []
      counter = 1
      while counter <= numRows:
         row = []
         if counter <= 2: 
            for i in range(counter):
               row.append(1)
            res.append(row)
         else:
            row.append(1)
            for i in range(0, counter-2):
               temp = res[counter- 2][i] + res[counter- 2][i+1]
               row.append(temp)
            row.append(1)
            res.append(row)
         counter += 1
      return res