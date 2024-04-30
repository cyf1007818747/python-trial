from typing import List

# AC
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if not temp:
                temp = intervals[i]

            if intervals[i][0] <= temp[1]:
                temp[1] = max(temp[1], intervals[i][1])
            else:
                ans.append([temp[0], temp[1]])
                # logic error # *
                # // temp = None
                temp = intervals[i]
        
        if temp:
            ans.append([temp[0], temp[1]])

        return ans
