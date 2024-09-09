class Solution:
   def strStr(self, haystack: str, needle: str) -> int:
      if not needle:  # if needle is an empty string, return 0
         return 0
      i_haystack = 0
      while i_haystack <= len(haystack) - len(needle):  # ensure there's enough space for needle in haystack
         i_needle = 0
         start = i_haystack
         while i_needle < len(needle) and haystack[i_haystack + i_needle] == needle[i_needle]:
            i_needle += 1
         if i_needle == len(needle):  # full match found
            return start
         i_haystack += 1  # move to the next character in haystack
      return -1  # needle not found
