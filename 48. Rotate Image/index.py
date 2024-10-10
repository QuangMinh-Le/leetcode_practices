from typing import List


class Solution:
   def rotate(self, matrix: List[List[int]]) -> None:
      """
      Do not return anything, modify matrix in-place instead.
      """
      length = len(matrix)
      # Transpose the matrix
      for i in range(length):
          for j in range(i, length):
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      # Reverse each row
      for i in range(length):
          matrix[i].reverse()