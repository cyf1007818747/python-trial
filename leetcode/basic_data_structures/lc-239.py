from typing import List

# use priority queue / heap (after seeing .cn solution)
# start to AC - 14:02
# AC
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq # cannot use queue.priorityQueue(), since it does not support the top look up action
        pq = []

        # push number and index
        # python heap put smallest element at the top
        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))

        # heapify pq
        # this heapify step is redundant, since you use heappush above
        # only choose one of them is enough # *
        heapq.heapify(pq)

        ans = [-pq[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            while pq[0][1] <= i - k:
                heapq.heappop(pq)

            ans.append(-pq[0][0])

        return ans

# use monotonic stack (after seeing .cn solution)
# start to AC - 6:37
# AC
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        ans = []

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

        ans.append(nums[q[0]])

        for i in range(k, len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            while q[0] <= i - k:
                q.remove(q[0])

            ans.append(nums[q[0]])

        return ans

# use monotonic queue, but use collestions.queue() instead of list to improve performance
class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        q = deque()
        ans = []

        for i in range(k):
            # always be super clear of the logic !!
            # // while q and nums[q[0]] <= nums[i]:
            while q and nums[q[-1]] <= nums[i]:
                # // q.popleft()
                q.pop()
            
            q.append(i)
        
        ans.append(nums[q[0]])

        for i in range(k, len(nums)):
            # // while q and nums[q[0]] <= nums[i]:
            while q and nums[q[-1]] <= nums[i]:
                # // q.popleft()
                q.pop()

            q.append(i)

            while q[0] <= i - k:
                q.popleft()

            ans.append(nums[q[0]])

        return ans
