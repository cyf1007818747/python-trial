from typing import List

# original solution, uses 2 min
# passed all leetcode tests
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rtn = 0

        for i in nums:
            rtn ^= i

        return rtn