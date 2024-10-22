class Solution:
   def titleToNumber(self, columnTitle: str) -> int:
      result = 0
      # Iterate over each character in the columnTitle string
      for char in columnTitle:
          # Convert the character to its corresponding number (A=1, B=2, ..., Z=26)
          result = result * 26 + (ord(char) - ord('A') + 1)
      return result
         
         
      