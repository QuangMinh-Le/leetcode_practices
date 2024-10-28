from typing import List


class Solution:
   def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      # Initialize a set to keep track of elements within a window of size `k`
      recent_elements = set()
      
      for i in range(len(nums)):
          # If nums[i] is already in the set, then we found a nearby duplicate
          if nums[i] in recent_elements:
              return True
          
          # Add the current element to the set
          recent_elements.add(nums[i])
          
          # Ensure the set size does not exceed `k`
          if len(recent_elements) > k:
              recent_elements.remove(nums[i - k])
      
      # No nearby duplicates found within the distance `k`
      return False