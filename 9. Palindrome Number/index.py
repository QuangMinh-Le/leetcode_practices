class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        else:
            divider = len(str(x))//2
            counter = 0
            while counter <= divider & int(str(x)[counter]) == int(str(x)[-1 -counter]):
               counter += 1
            if counter == divider:
               return True
            else:
               return False
           