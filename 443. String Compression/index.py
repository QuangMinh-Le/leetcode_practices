from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Index to write compressed characters
        read = 0  # Index to read original characters
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # Return the length of the compressed string
        return write
