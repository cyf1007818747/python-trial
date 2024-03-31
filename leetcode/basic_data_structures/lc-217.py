from typing import List

# data structure: set

# passed all leetcode cases
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        
        for num in nums:
            if num not in elements:
                elements.add(num)
            else:
                return True
                
        return False