from typing import List

# data structure: stack

# ! recite !!
# this is you recite and rewrite from leetcode.cn
# passed all leetcode tests
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)

        rtn = [0] * length

        stack = []

        for i in range(length):
            temp = temperatures[i]
            
            while stack and temp > temperatures[stack[-1]]:
                index_top = stack.pop()
                rtn[index_top] = i - index_top

            stack.append(i)

        return rtn
    
# todo: practice more on monotonic stack