# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
   def firstBadVersion(self, n: int) -> int:
      l, r = 1, n
      while l < r:
          v = (l + r) // 2
          if isBadVersion(v):
              r = v
          else:
              l = v + 1
      return l
            