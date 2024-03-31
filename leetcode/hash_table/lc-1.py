from typing import List

# given nums >= 2
# if len nums == 2: return nums
# use a dict to store num: index
# iterate nums, for index i, the other number is target - nums[i], find whether this is in the dict
# > if in the dict, return i, dict[target-nums[i]]
# > else dict[nums[i]] = i
# for each i, only consider numbers before it

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        table = dict()

        for i in range(len(nums)):
            the_other_index = table.get(target-nums[i])
            # * wrong, since 'if 0:' evaluates to false in python
            # // if the_other_index:
            if the_other_index is not None:
                return [i, the_other_index]
            
            table[nums[i]] = i

        return[-1, -1] # never happens


sol = Solution()
nums = [2,7,11,15]
target = 9
rtn = sol.twoSum(nums, target)
print('rtn:', rtn)