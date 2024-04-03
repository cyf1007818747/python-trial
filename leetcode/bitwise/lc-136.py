from typing import List

# original solution, uses 2 min
# passed all leetcode tests
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rtn = 0

        for i in nums:
            rtn ^= i

        return rtn
    

# use reduce function
# passed all leetcode tests
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce

        return 0^reduce(lambda x, y: x^y, nums)