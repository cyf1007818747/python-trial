from typing import List

# modify nums in-place after reviewing .cn solution
# [3,4,-1,1], n = 4
# [-3,4,-5,-1] return 2
# start to AC with oral presentation - 14:38
# AC
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n is the len of nums
        n = len(nums)

        # 1. make all non-positive numbers to be n + 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 2. iterate nums. for each num
        # > if |num| <= n: make nums[abs(num)-1] to be -nums[num-1], as a marker
        for i in range(n):
            if abs(nums[i]) <= n and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = - nums[abs(nums[i]) - 1]

        # 3. iterate nums, for the first positive number index i, return i + 1
        # if no positive number, return n + 1
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
