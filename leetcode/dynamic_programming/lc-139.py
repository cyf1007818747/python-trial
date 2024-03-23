from typing import List

# constraint: no empty string
# dynamic programming
# dp[i]: whether substr(0, i) can be segemented
# transfer equation:
# > for any 0 < j < max len word in wordDict
# > if substr(j, i) in dict and dp[i - j] is true, then dp[i] is true
# > else dp[i] is false
def wordBreak(s: str, wordDict: List[str]) -> bool:
    # longest_str = max(wordDict, key=len) # *
    max_str_len = len(max(wordDict, key=len)) #*

    # print("-- max_str_len: ", max_str_len)
    
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(min(i + 1, max_str_len + 1)):
            # check whether:
            # > the substring of s that has length j and ends at position i - 1 (incl) is in the dict
            # > and
            # > whether the substr that ends 1 position before the substr is in the dict
            if s[i - j: i] in wordDict and dp[i - j]:
                dp[i] = True
                break

    return dp[-1]

# make the index mapping less confused
# passed all leetcode tests
def wordBreak_lessedConfused(s: str, wordDict: List[str]) -> bool:
    if s in wordDict:
        return True
    
    max_str_len = len(max(wordDict, key=len))

    dp: List[bool] = [False] * len(s)

    # check the first element
    dp[0] = s[0] in wordDict

    for i in range(1, len(s)):
        for j in range(min(i + 2, max_str_len + 1)):
            if s[i+1-j:i+1] in wordDict and ((i - j < 0) or dp[i - j]):
                dp[i] = True
                break
    
    return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
output = wordBreak_lessedConfused(s, wordDict)
print("#### output: ", output)
