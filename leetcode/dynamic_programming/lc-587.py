# given: both lengths >= 1

# dp[i][j]: len longest common substring ends at word1[i-1] and word2[j-1]
# > if word1[i-1] == word1[j-1]: dp[i][j] = dp[i-1][j-1] + 1
# > else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# get the max length of common substring
# return len word1 + len word2 - 2 * len max common string
# passed all leetcode tests
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        # dp[1][1] = 1 if word1[0] == word2[0] else 0

        max_common_str_len = 0

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                max_common_str_len = max(max_common_str_len, dp[i][j])

        print("dp:", dp)

        return len(word1) + len(word2) - 2 * max_common_str_len

# reduce space complexity
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        prev_row = [0 for j in range(len(word2) + 1)]
        curr_row = [0 for j in range(len(word2) + 1)] 

        # dp[1][1] = 1 if word1[0] == word2[0] else 0

        max_common_str_len = 0

        for i in range(1, len(word1) + 1):
            # print("curr_row:", curr_row)
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    # dp[i][j] = dp[i-1][j-1] + 1
                    curr_row[j] = prev_row[j-1] + 1
                else:
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    curr_row[j] = max(prev_row[j], curr_row[j-1])
                max_common_str_len = max(max_common_str_len, curr_row[j])
            # prev_row = curr_row # ! you spend so long to find this mistake
            prev_row = curr_row.copy() # very important !! # *

        # print("prev_row:", prev_row)
        # print("curr_row:", curr_row)

        return len(word1) + len(word2) - 2 * max_common_str_len
    
word1, word2 = "intention", "execution"
sol = Solution2()
rtn = sol.minDistance(word1, word2)
print("rtn:", rtn)