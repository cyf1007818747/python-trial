
# given: n >= 2
# dp[i] denotes max product till integer i
# dp[i] = max(1*dp[i-1], 2*dp[i-2], ... j*dp[i-j]), for i >= 2 and i - j >= 2
# passed all test cases
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        
        dp = [0] * (n + 1)

        dp[0:3] = [0, 0, 1]

        for i in range(3, n + 1):
            for j in range(1, i - 1):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))

        # print(dp)
        
        return dp[n]
    
n = 10
sol = Solution()
rtn = sol.integerBreak(n)
print('rtn:', rtn)

