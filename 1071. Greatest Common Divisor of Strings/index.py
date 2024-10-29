from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 is the same as str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate the gcd of the lengths of str1 and str2
        gcd_len = gcd(len(str1), len(str2))
        
        # The GCD string would be the prefix of str1 up to gcd_len
        return str1[:gcd_len]