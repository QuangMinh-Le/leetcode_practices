class Solution:
   def freqAlphabets(self, s: str) -> str:
      ## Initial Solution of Quang Minh Le
      # s += "a"
      # res = ""
      # raw = s.split("#")
      # for each in raw: 
      #    if len(each) == 2:
      #       res += chr(int(each)+64).lower()
      #    if len(each) > 2:
      #       if each [-1] == "a": 
      #          each = each[:-1]
      #          for i in range(0, len(each), 1):
      #             res += chr(int(each[i])+64).lower()
      #       else:
      #          for i in range(0, len(each) - 2, 1):
      #             res += chr(int(each[i])+64).lower()
               
      #          res += chr(int(each[len(each) - 2:])+64).lower()
      #    if each == "a":
      #       continue
      # return res
      
      
      ## More optimized solution
   
      res = []
      i = 0

      while i < len(s):
         if i + 2 < len(s) and s[i + 2] == '#':
            val = int(s[i: i + 2])
            res.append(chr(val + 96)) # chr(65 - 90) is 'A' to 'Z', chr(97 - 122) is 'a' to 'z'
            i += 3
         else:
            res.append(chr(int(s[i]) + 96))
            i += 1

      return ''.join(res)