from typing import List

#  0 1 2 3 4 5 6 7 8
# [1,1,2,3,3,4,4,8,8]
# passed all test cases on leetcode
def singleNonDuplicate(nums: List[int]) -> int:
    numsLen = len(nums)
    if numsLen == 1:
        return nums[0]
    
    # @assert: numsLen >= 3

    # a helper function telling whether the element is to the left, right or at the index i
    # returns -1, 0 or 1
    def checkIndex(i: int) -> int:
        # > first element
        if i == 0:
            return 0 if nums[i] != nums[i+1] else 1
        # > last element
        if i == numsLen - 1:
            return 0 if nums[i] != nums[i-1] else -1
        # > else (middle elements)
        # >> equals prev: i is odd => 1, i is even => -1
        if nums[i] == nums[i-1]:
            return -1 if i % 2 == 0 else 1
        # >> equals next: i is odd => -1, i is even => 1
        elif nums[i] == nums[i+1]:
            return 1 if i % 2 == 0 else -1
        # >> else (equals neither) => 0
        else:
            return 0
        
    l, r = 0, numsLen - 1
    while (l <= r):
        mid = l + (r - l) // 2 # *
        relativePos = checkIndex(mid)
        if relativePos == 0:
            return nums[mid]
        elif relativePos == -1:
            r = mid - 1
        else:
            l = mid + 1

    return -1

testList = [1,1,2,3,3,4,4,8,8]
output = singleNonDuplicate(testList)
print("#### output: ", output)


        

        
        