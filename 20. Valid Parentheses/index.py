class Solution:
    def isValid(self, s: str) -> bool:
      collection = {")":"(", 
                    "]":"[", 
                    "}": "{"}
      stack = []
      for c in s: 
         if c not in collection:
            stack.append(c)
            continue
         if not stack or stack[-1] != collection[c]:
            return False
         stack.pop()
      return not stack