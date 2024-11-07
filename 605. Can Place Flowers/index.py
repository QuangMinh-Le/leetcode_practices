from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            # Check if the current, previous, and next positions are empty (or bounds)
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # Plant a flower here
                flowerbed[i] = 1
                count += 1
                # Skip the next spot
                i += 2
            else:
                i += 1
                
            # Early return if we've planted enough flowers
            if count >= n:
                return True
        
        return count >= n
