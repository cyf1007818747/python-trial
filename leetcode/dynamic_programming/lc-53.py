
from typing import List

# let dp[i] denotes the largest subarray ends at position i-1
# passed all leetcode tests
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)

# reduce space complexity
# passed all leetcode tests
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [0] * len(nums)

        # dp[0] = nums[0]
        dp_cur = nums[0]
        max_dp_cur = dp_cur

        for i in range(1, len(nums)):
            # dp[i] = max(dp[i-1] + nums[i], nums[i])
            dp_cur = max(dp_cur + nums[i], nums[i])
            max_dp_cur = max(dp_cur, max_dp_cur)

        return max_dp_cur