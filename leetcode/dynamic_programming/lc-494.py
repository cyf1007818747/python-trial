from typing import List

# [1,1,1,1,1] 
# fst - scd = target
# fst + scd = sum
# scd = (sum - target) // 2

# finished after looking at .cn solution
# AC
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # if (sum - target) % 2 != 0 or < 0, then does not exist
        # dp[i][j]: num ways to arrange first i elements that sums to j
        # dp[0][k] = 0 
        # > if choose nums[i], dp[i][j] = dp[i-1][j-nums[i]]
        # > if not choose nums[i], dp[i][j] = dp[i-1][j]
        # sum the 2 above
        summ = sum(nums)
        if (summ - target) % 2 != 0 or (summ - target) < 0:
            return 0

        goal = (summ - target) // 2

        dp = [[0] * (goal + 1) for i in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(0, goal + 1):
                num_ways = 0
                if j - nums[i-1] >= 0: # *
                    num_ways += dp[i-1][j-nums[i-1]] 
                num_ways += dp[i-1][j]
                dp[i][j] = num_ways

        return dp[-1][-1]
