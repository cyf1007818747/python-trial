from typing import List

# original solution
# start to AC - 9:20
# AC
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > len(nums) // 2:
                return num

        return nums[0]
    

# use divide and conquer approach (WBYS after reading .cn)
# AC
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majorityElementSublist(start, end) -> int:
            if start > end:
                return 0
            
            if start == end:
                return nums[start]

            mid = start + (end - start) // 2
            
            leftMajority = majorityElementSublist(start, mid)
            rightMajority = majorityElementSublist(mid+1, end)

            countl, countr = 0, 0

            for num in nums[start:end+1]:
                if num == leftMajority:
                    countl += 1
                if num == rightMajority:
                    countr += 1

            return leftMajority if countl > countr else rightMajority

        return majorityElementSublist(0, len(nums) - 1)
