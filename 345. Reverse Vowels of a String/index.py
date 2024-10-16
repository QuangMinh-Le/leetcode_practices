class Solution:
   def reverseVowels(self, s: str) -> str:
      if len(s) == 1: 
         return s
      
      # Using set to access faster
      vowels = set({"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}) 
      collection = []
      index = []
      temp = list(s)
      
      for i in range(len(s)): 
         if s[i] in vowels: 
               collection.append(s[i])
               index.append(i)
               
      collection.reverse()
      
      for y in range(len(collection)): 
         
         # Convert string to list --> able to modify by index
         temp[index[y]] = collection[y]
      res = ''.join(temp)
      return res