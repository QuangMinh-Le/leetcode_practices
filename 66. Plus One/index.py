from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count_from_bottom = -1
        while count_from_bottom >= -len(digits):  # Iterate through digits from the last
            if digits[count_from_bottom] == 9:  # If the digit is 9, set it to 0
                digits[count_from_bottom] = 0
                count_from_bottom -= 1
            else:
                digits[count_from_bottom] += 1  # Increment the current digit
                return digits  # Return the updated list immediately
        
        # If we exit the loop, it means all digits were 9
        digits.insert(0, 1)  # Add 1 at the beginning (carry)
        return digits