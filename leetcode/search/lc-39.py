from typing import List

# use backtracking:
# each time, increase the frequency of one number by one, and continue to search until
# the overall sum > target
# start to AC - 15:37
# AC, but very slow
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = set()

        def backtrack(freq: List[int]):
            summ = sum([ candidates[i] * freq[i] for i in range(n)])
            if summ > target:
                return
            if summ == target:
                combinations = []
                for i in range(n):
                    if freq[i] != 0:
                        combinations += [candidates[i]] * freq[i]
                ans.add(tuple(combinations))
                return
            
            for i in range(n):
                freq[i] += 1
                backtrack(freq)
                freq[i] -= 1

        freq = [0] * n
        backtrack(freq)
        return [ comb for comb in ans ]
    
# simpler backtracking after reviewing .cn solution
# start to AC - 15:07
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def backtrack(combinations: List[int], idx: int, summ: int):
            if summ > target or idx >= n:
                return
            if summ == target:
                ans.append(combinations)
                return
            
            backtrack(combinations, idx + 1, summ)
            backtrack(combinations+[candidates[idx]], idx, summ + candidates[idx])
            
        backtrack([], 0, 0)
        
        return ans

# simpler backtracking after reviewing .cn solution - save space
# AC
class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        combinations = []

        def backtrack(idx: int, summ: int):
            if summ > target or idx >= n:
                return
            if summ == target:
                # *
                # // ans.append(combinations)
                ans.append(combinations.copy())
                return
            
            backtrack(idx + 1, summ)
            combinations.append(candidates[idx])
            backtrack(idx, summ + candidates[idx])
            combinations.pop()
            
        backtrack(0, 0)
        
        return ans
