from typing import List

# len nums <= 1, return len(nums)

# find the max frequency num(s)
# > if only one max freq: find the first and last appeared index, length is the diff
# > if more than one, find all diffs and get the min diff

# [0, 9, 2, 3, 4, 9, 9, 7]

# initial solution
# passed all leetcode cases
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        
        max_freq = 0
        most_freq_nums = [nums[0]]
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_freq:
                max_freq = freq[num]
                most_freq_nums = [num]
            elif freq[num] == max_freq:
                most_freq_nums.append(num)
                
        
        smallest_length = float('inf')
        
        for n in most_freq_nums:
            subarr_len = len(nums) - nums[::-1].index(n) - nums.index(n)
            smallest_length = min(smallest_length, subarr_len)
            
        return smallest_length
    

# TODO: record the first and last index at the intial iteration