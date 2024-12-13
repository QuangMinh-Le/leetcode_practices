class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_count = 0
        temp = ''
        
        for each in s:
            if each not in temp:
                temp += each
            else:
                # Update the longest count if needed
                longest_count = max(longest_count, len(temp))
                # Remove characters up to the duplicate to maintain uniqueness
                temp = temp[temp.index(each) + 1:] + each
        
        # Final check for the longest substring after the loop
        longest_count = max(longest_count, len(temp))
        
        return longest_count