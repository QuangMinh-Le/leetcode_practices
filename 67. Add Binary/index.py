class Solution:
   def addBinary(self, a: str, b: str) -> str:
      res = ""
      decimal_a = int(a, 2)
      decimal_b = int(b, 2)
      somme = decimal_a + decimal_b
      res = f"{bin(somme)[2:]}"
      return res
        