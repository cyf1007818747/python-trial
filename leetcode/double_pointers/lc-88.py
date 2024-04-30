from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        
        if n == 0:
            return
    
        sorted_list = [0] * (m + n)
        p1, p2 = 0, 0
        cur = 0

        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                sorted_list[cur] = nums1[p1]
                p1 += 1
            else:
                sorted_list[cur] = nums2[p2]
                p2 += 1
            cur += 1
        
        if p1 < m:
            # // sorted_list[cur:] = nums1[p1:]
            # // sorted_list[cur:] = nums1[p1:m+1]
            sorted_list[cur:] = nums1[p1:m]
        if p2 < n:
            sorted_list[cur:] = nums2[p2:]

        nums1[:] = sorted_list[:]
