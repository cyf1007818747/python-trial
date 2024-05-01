
# start to AC - 4:12
# AC
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev2, prev = 1, 2
        cur = 0
        # // for i in (2, n-1):
        for i in range(2, n):
            cur = prev2 + prev
            prev2 = prev
            prev = cur

        return cur
