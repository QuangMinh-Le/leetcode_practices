class Solution:
   def reverse(self, x: int) -> int:
      # Define the 32-bit integer range
      INT_MIN, INT_MAX = -2**31, 2**31 - 1
      
      # Determine the sign of the number
      sign = -1 if x < 0 else 1
      x = abs(x)
      
      # Reverse the digits
      reversed_str = str(x)[::-1]
      reversed_int = sign * int(reversed_str)
      
      # Check for overflow
      if reversed_int < INT_MIN or reversed_int > INT_MAX:
          return 0
      return reversed_int