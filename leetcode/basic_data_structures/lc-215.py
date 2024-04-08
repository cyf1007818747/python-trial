from queue import PriorityQueue
from typing import List

# priority queue of length k
# for each num in nums:
# insert num into pq
# > if len(pq) > k: pop the smallest element
# eventually, the top of pq is the required kth largest
# AC, but runnign time is large
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        
        for num in nums:
            pq.put(num)
            if pq.qsize() > k:
                pq.get()

        return pq.get()
    

# use bucket ranking
# given: nums[i] is in range -10000 to 10000 inclusive

# have a bucket to count the frequency of each number, from low to high
# iterate from the highest and get the kth (by decreasing k)
# AC and running time is low
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq_bucket = [0] * 20001
        
        for num in nums:
            freq_bucket[num + 10000] += 1

        for i in range(20000, -1, -1):
            k -= freq_bucket[i]
            # for the k == 0 case, use a concrete example to check
            # * recite: we should inclue the edge case for bucket ranking
            if k <= 0:
                return i - 10000

        return 0
    

# use divide conquer partial sort approach (very complex, just to practice)
# passed 40/41 lc cases, the only one is due to space complexity (since you )
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def partialSort(nums, l, r, k):
        # > if l == r, return
        # > else mid = (l+r) // 2
        # >> if k in l to mid, partialSort l to mid
        # >> if k in mid+1 to r, we partial Sort mid+1 to r
        # >> else: do nothing
        def partialSort(l, r):
            if l >= r:
                return

            nonlocal k, nums
            if not l <= len(nums) - k <= r:
                return

            fst, scd = nums[l], nums[l+1]
            # print('fst:', fst, 'scd:', scd)

            smaller, larger = sorted([fst, scd])
            th = max(fst, scd)

            
            left_subl = [smaller]
            right_subl = [larger]

            for i in range(l+2, r+1):
                if nums[i] < th:
                    left_subl.append(nums[i])
                else:
                    right_subl.append(nums[i])

            
            nums[l:l+len(left_subl)] = left_subl
            nums[l+len(left_subl):r+1] = right_subl

            if len(nums) - k < l+len(left_subl):
                partialSort(l, l+len(left_subl)-1)
            else:
                partialSort(l+len(left_subl), r)

        partialSort(0, len(nums)-1)
        
        return nums[-k]
