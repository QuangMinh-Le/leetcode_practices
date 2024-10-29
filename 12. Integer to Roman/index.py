class Solution:
      def intToRoman(self, num: int) -> str:
         roman = {1000: "M",
                  500: "D",
                  100: "C",
                  50: "L",
                  10: "X",
                  5: "V" ,
                  1: "I"
                  }
         
         res = ""
         for i in roman:
            if i in [1000, 100, 10 ,1]:
               adder = num // i
               remainder = num % i

               if adder > 0 and adder < 4:
                  for j in range(adder):
                     res += roman[i]
                  num = remainder
            else: 
               adder = num // i
               remainder = num % i

               if adder == 1 and remainder < 4*2*i:
                  res += roman[i]
               elif adder == 1 and remainder == 4:
                  res += roman
         return res