from typing import List

# either rob or do not rob the first house
# dp[i]: max amount of money you can rob for houses 0 to i inclusive
# for house i
# > if rob, cannot rob i - 1, total money = dp[i-2] + nums[i]
# > if not rob, total money = dp[i-1]

# if rob the first house: dp[0] = nums[0], dp[1] = dp[0], dp[-1] = dp[-2]
# if not rob the first house: dp[0] = 0, dp[1] = nums[1]
# passed all leetcode tests
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        # rob the first house
        dp[0] = nums[0]
        dp[1] = dp[0]
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        dp[-1] = dp[-2]
        max_rob_the_first = dp[-1]

        # do not rob the first house
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(max_rob_the_first, dp[-1])

# reduce space complexity by using status pointers (prev2, prev and cur)
# very hard to think !! not recommended ! better use solution 3
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # rob the first
        dp_prev2, dp_prev = nums[0], nums[0]
        dp_cur = nums[0] if len(nums) == 3 else max(dp_prev, dp_prev2 + nums[2])
        # print('dp_prev2', dp_prev2, 'dp_prev', dp_prev, 'dp_cur:', dp_cur)
        for i in range(3, len(nums) - 1):
            dp_prev2, dp_prev = dp_prev, dp_cur
            dp_cur = max(dp_prev, dp_prev2 + nums[i])
            # print('dp_prev2', dp_prev2, 'dp_prev', dp_prev, 'dp_cur:', dp_cur)
        
        max_when_rob_first = dp_cur

        # do not rob the first
        dp_prev2, dp_prev = 0, nums[1]
        dp_cur = max(dp_prev, dp_prev2 + nums[2])
        # print('----dp_prev2', dp_prev2, 'dp_prev', dp_prev, 'dp_cur:', dp_cur)
        for i in range(3, len(nums)):
            dp_prev2, dp_prev = dp_prev, dp_cur
            dp_cur = max(dp_prev, dp_prev2 + nums[i])
            # print('----dp_prev2', dp_prev2, 'dp_prev', dp_prev, 'dp_cur:', dp_cur)

        return max(max_when_rob_first, dp_cur)


# reduce space complexity by directly modifying original dp
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # dp = [0] * len(nums)

        # rob the first house
        dp_i_2 = nums[0] # dp[0] = nums[0]
        dp_i_1 = dp_i_2 # dp[1] = dp[0]
        dp_i = 0 if len(nums) > 3 else dp_i_1 # this condition check is special for this question
        for i in range(2, len(nums) - 1):
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            dp_i = max(dp_i_1, dp_i_2 + nums[i])
            # prevent the sliding window to proceed at last pos
            if i != len(nums) - 2:
                dp_i_2, dp_i_1 = dp_i_1, dp_i 

        max_rob_the_first = dp_i

        # do not rob the first house
        dp_i_2 = 0 # dp[0] = nums[0]
        dp_i_1 = nums[1] # dp[1] = dp[0]
        dp_i = 0
        for i in range(2, len(nums)):
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            dp_i = max(dp_i_1, dp_i_2 + nums[i])
            # prevent the sliding window to proceed at last pos
            if i != len(nums) - 1:
                dp_i_2, dp_i_1 = dp_i_1, dp_i

        return max(max_rob_the_first, dp_i)


nums = [200,3,140,20,10]
sol = Solution2()
rtn = sol.rob(nums)
print("rtn:", rtn)
        
