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