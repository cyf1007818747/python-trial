from typing import List

# start to AC - 3:34
# AC
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign_is_positive = True # can be sign = 1

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign_is_positive = not sign_is_positive # can be sign = -sign

        return 1 if sign_is_positive else -1
