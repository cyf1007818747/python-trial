
# use sliding window approach
# AC
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        # // charSet = set(s[0])
        charSet = set([s[0]])
        maxlen = 0
        r = 0
    
        for i in range(len(s)):
            while r + 1 < len(s) and s[r+1] not in charSet:
                r += 1
                charSet.add(s[r])

            maxlen = max(maxlen, len(charSet))
            charSet.remove(s[i])

        return maxlen
