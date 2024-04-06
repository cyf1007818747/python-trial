from typing import List

# backtracking and mask after reading .cn official solution
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []

        for word in arr:
            mask = 0
            for c in word:
                idx = ord(c) - ord('a')
                # c already in the mask => word contains duplicate chars, abandon
                if ((1 << idx) & mask):
                    mask = 0
                    break
                mask = mask | (1 << idx)
                # you cannot append for every update of the mask
                # // masks.append(mask)

            if mask != 0:
                masks.append(mask)

        ans = 0

        def backtrack(pos, msk):
            # all msks in the masks are checked for this path
            if pos == len(masks):
                num_chars = 0
                while msk:
                    if msk & 1:
                        num_chars += 1
                    # this does not change the msk value # *
                    # // msk >> 1
                    msk >>= 1 # *
                nonlocal ans
                ans = max(ans, num_chars)

                # more concise apporach instead of using num_chars
                # ans = max(ans, bin(mask).count("1"))
                
                return

            # for each position, check all possibilities of add (if possible) or not add
            if masks[pos] & msk == 0:
                backtrack(pos+1, masks[pos] | msk)

            backtrack(pos+1, msk)

        backtrack(0, 0)

        return ans
