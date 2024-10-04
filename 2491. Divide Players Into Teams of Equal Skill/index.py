from typing import List


class Solution:
   def dividePlayers(self, skill: List[int]) -> int:
      skill.sort()
      
      number_teams = len(skill) // 2
      total_skill = sum(skill)
      
      # Ideal skill sum for each team (total skill divided by number of teams)
      if total_skill % number_teams != 0:
          return -1
      ideal_total_skill = total_skill // number_teams
      
      sum_chemistry = 0
      
      # Two-pointer technique to find pairs
      left, right = 0, len(skill) - 1
      
      while left < right:
          if skill[left] + skill[right] != ideal_total_skill:
              return -1
          sum_chemistry += skill[left] * skill[right]
          left += 1
          right -= 1
      
      return sum_chemistry