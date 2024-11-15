from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      # Calculate the sum of the first k elements
      curSum = sum(nums[:k])
      # Initialize maxSum as the current sum
      maxSum = curSum
      
      # Slide the window through the rest of the array
      for i in range(k, len(nums)):
          curSum += nums[i] - nums[i - k]
          maxSum = max(maxSum, curSum)
      
      # Return the maximum average
      return maxSum / k