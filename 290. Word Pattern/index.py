class Solution:
   def wordPattern(self, pattern: str, s: str) -> bool:
      checker = {}
      checker_value = []
      string = s.split()
      if len(pattern) != len(string):
         return False
      else: 
         for i in range(len(pattern)):
            if pattern[i] not in checker: 
               if string[i] not in checker_value: 
                  checker_value.append(string[i])
                  checker[pattern[i]] = string[i]
               else:
                  return False
            if pattern[i] in checker: 
               if checker[pattern[i]] != string[i]:
                  return False
      return True