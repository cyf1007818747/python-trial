from typing import List

# start to pass majority cases - 17:53
# passed 309 / 313 cases, the failed ones are due to time exceed, so should be functionally correct
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        twoSumDic = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                twoSum = nums[i] + nums[j]
                if twoSumDic.get(twoSum) != None:
                    twoSumDic[twoSum].append((i, j))
                else:
                    twoSumDic[twoSum] = [(i, j)]

        ans = set()

        # you made this mistake many times # *
        # // for idx in nums: 
        for idx in range(len(nums)): 
            num = nums[idx]
            if twoSumDic.get(-num):
                for i, j in twoSumDic.get(-num):
                    if idx != i and idx != j:
                        # cannot add mutable type to a set !! # *
                        # // ans.add(set([num, nums[i], nums[j]])) 
                        # // ans.add(sorted([num, nums[i], nums[j]])) 
                        # details !!
                        # // ans.add(tuple(sorted([num, i, j])))
                        ans.add(tuple(sorted([num, nums[i], nums[j]]))) 

        ans = [triple for triple in ans]

        return ans
    

# another solution that uses the number of occurences of numbers
# takes 27:00 until passed 308 / 313 cases, but for some cases still exceeds time
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        occurences = {}

        for i in range(len(nums)):
            if occurences.get(nums[i]) != None:
                if occurences[nums[i]] < 3:
                    occurences[nums[i]] += 1
            else:
                occurences[nums[i]] = 1

        twoSums = {}
        # allow repeats
        for n1 in occurences:
            for n2 in occurences:
                sum2 = n1 + n2
                # //if twoSums[sum2] == None:
                if twoSums.get(sum2) == None: 
                    twoSums[sum2] = [(n1, n2)]
                else:
                    twoSums[sum2].append((n1, n2))
        
        ans = set()
        for i in range(len(nums)):
            # // if twoSums.[-nums[i]] == None:
            if twoSums.get(-nums[i]) == None:
                continue
            
            # * very good backtracking trick here (good that you figure it out by yourself)
            for n1, n2 in twoSums[-nums[i]]:
                occurences[nums[i]] -= 1
                occurences[n1] -= 1
                occurences[n2] -= 1

                if occurences[nums[i]] >= 0 and occurences[n1] >= 0 and occurences[n2] >= 0:
                    # sorted cannot take 3 arguments like sorted(n1, n2, n3), you made this mistake many times # *
                    # // ans.add(tuple(sorted(nums[i], n1, n2))) # *
                    ans.add(tuple(sorted([nums[i], n1, n2])))

                occurences[nums[i]] += 1
                occurences[n1] += 1
                occurences[n2] += 1

        return [[num for num in triple] for triple in ans]
    

# use l, r pointers
# slow due to your set operation and transfer set into list
# start to AC - 15:00
# AC but uses 2252 ms
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ans = set()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            target = -nums[i]

            # // while l <= r and l < len(nums) and r >= 0:
            while l < r and l < len(nums) and r >= 0: # details !! # *
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    # // ans.add(tuple(i, l, r))
                    # fully and deepy understand the question !! the question wants number not index # *
                    ans.add(tuple([nums[i], nums[l], nums[r]])) 
                    l += 1
                    r -= 1

        return [[num for num in triple] for triple in ans]


# use l, r pointers
# improves running time (by avoiding using set and transferring set into list)
# the trick to not use set it to continue the loop if nums[i] == nums[i-1]
# AC, running time 887 ms
class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print('sorted nums:', nums)

        ans = []
        for i in range(len(nums)):
            # edge case (a little bit hard to figure out) # *
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            l, r = i+1, len(nums) - 1
            target = -nums[i]

            while l < r and l < len(nums) and r >= 0:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # print('answer {} added. i: {}, l: {}, r: {}'.format(ans[-1], i, l, r))
                    l += 1
                    r -= 1

                    # you made the order wrong many times # *
                    # // while nums[l] == nums[l-1] and l < len(nums):
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    # // while nums[r] == nums[r+1] and r >= 0
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
                    if l >= r or l >= len(nums) or r < 0:
                        break

        return ans
