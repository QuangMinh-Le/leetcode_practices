class Solution:
   def makeFancyString(self, s: str) -> str:
      if len(s) < 3: 
         return s
      res = []
      res.append(s[0])
      res.append(s[1])
      for char in s[2:]: 
         if char == res[-1] and char == res[-2]:
            continue
         else: 
            res.append(char)
      return ''.join(res)
            