from typing import List

# data structure: hash table / dict

# passed all leetcode cases
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        
        # this is for the case to include all nums from nums[0] # *
        # ! just recite for now that this is common for prefix sum questions
        sum_freq = {0: 1}

        summ, count = 0, 0

        for num in nums:
            summ += num
            count += sum_freq.get(summ - k, 0)
            sum_freq[summ] = sum_freq.get(summ, 0) + 1

        return count