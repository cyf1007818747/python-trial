# original solution, uses 4:27
# passed all leetcode tests
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        
        ans = ""
        for wd in s[::-1]:
            ans += wd + " "
        return ans.strip()
    
# do not use python built in functions
# double pointers
# from start to AC - uses 9:45
# AC
class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, 0
        
        while s[l] == ' ':
            l += 1

        # Do not choose too short / concise names, since it is very easy to mix them up and make mistakes
        # next time use start and end
        r = l

        ans = ""

        while l < len(s) and r < len(s):
            # ! wrong
            # // while s[r] != ' ' and r < len(s) 
            # always check index range first, otherwise there will be index out of bound error
            while r < len(s) and s[r] != ' ':
                r += 1

            ans = ' ' + s[l:r] + ans

            while r < len(s) and s[r] == ' ': 
                r += 1

            l = r

        if ans[0] == ' ':
            ans = ans[1:]

        return ans
