class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        initial = columnNumber
        while initial > 0: 
            res = chr(ord('A') + (initial - 1)%26) + res

            initial = (initial-1) // 26
        return res
        