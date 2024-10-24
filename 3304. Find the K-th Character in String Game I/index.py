class Solution:
   def kthCharacter(self, k: int) -> str:
      alphabet = []
      for i in range(65,91):
         alphabet.append(chr(i).lower())
      word = "a"
      
      while len(word) < k: 
         generated = "" 
         for char in word: 
            index = alphabet.index(char)
            generated += alphabet[index+1]
         word = word + generated
      
      return word[k-1]
                
      