        
class Solution:
   def mergeAlternately(self, word1: str, word2: str) -> str:
      res = ""
      length_1 = len(word1)
      length_2 = len(word2)
      
      collap = 0
      
      if length_1 > length_2:
         collap = length_2
         for i in range(collap):
            res += word1[i]
            res += word2[i]
         res += word1[collap:]
      
      if length_2 > length_1:
         collap = length_1
         for i in range(collap):
            res += word1[i]
            res += word2[i]
         res += word2[collap:]
         
      if length_2 == length_1:
         collap = length_1
         for i in range(collap):
            res += word1[i]
            res += word2[i]
      return res
      
         