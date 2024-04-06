# greedy approach after seeing .cn solution
# 1 1 7
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = [['a', a], ['b', b], ['c', c]]
        ans = ""

        while True:
            freq.sort(key=lambda x: -x[1])
            if freq[0][1] <= 0:
                break

            # the logic below is very tricky to think accurately # *
            if len(ans) < 2:
                ans += freq[0][0]
                freq[0][1] -= 1
            elif not freq[0][0] == ans[-1] == ans[-2]: # this consecutive equal is legal in python # *
                ans += freq[0][0]
                freq[0][1] -= 1
            elif freq[1][1] > 0 and not freq[1][0] == ans[-1] == ans[-2]:
                ans += freq[1][0]
                freq[1][1] -= 1
            elif freq[2][1] > 0 and not freq[2][0] == ans[-1] == ans[-2]:
                ans += freq[2][0]
                freq[2][1] -= 1
            else:
                break

        return ans
    

# rewrite by improving coding style after seeing .cn greedy approach
# start to AC - 9:11
# AC
class Solution2:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [['a', a], ['b', b], ['c', c]]
        ans = ""

        while True:
            counts.sort(key = lambda x: -x[1])
            stopLoop = True
            for i, (ch, cnt) in enumerate(counts): # *
                if cnt <= 0:
                    continue
                
                if (len(ans) >= 2 and ch == ans[-1] == ans[-2]):
                    continue

                ans += ch
                counts[i][1] -= 1
                stopLoop = False
                break # you forgot this again initially # *

            if stopLoop:
                break

        return ans
        