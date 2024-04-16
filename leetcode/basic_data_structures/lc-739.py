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
    
# this is you write a gain 2 wweks later
# start to AC - 11:53
# AC
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i - stack[-1]
                # details !!! # *
                # // ans.pop()
                stack.pop()
            
            stack.append(i)

        return ans
