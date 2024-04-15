from typing import List

# start to AC - 17:54
# AC
class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        
        while l < len(chars) and r < len(chars):
            # pay attention to index out of bound error when len(chars) changes

            while r < len(chars) - 1 and chars[r] == chars[r+1]:
                r += 1

            occurences = r - l + 1
            
            
            chars[l+1:r+1] = [] # *

            if occurences > 1:
                occur_str = str(occurences)
                # below is wrong because Python insert() will insert at the position and 
                # moves the original element back, not inserting after the original element at pos # *
                # // for c in occur_str: 
                # //   chars.insert(l, c)
                # //    l += 1
                for c in occur_str: 
                    l += 1
                    chars.insert(l, c)

            l += 1
            r = l

        return len(chars)

# do not use extra space to store occur_str
# start to AC - 8:15
# AC
class Solution2:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        
        while l < len(chars) and r < len(chars):
            # pay attention to index out of bound error when len(chars) changes

            while r < len(chars) - 1 and chars[r] == chars[r+1]:
                r += 1

            occurences = r - l + 1
            
            
            chars[l+1:r+1] = []

            if occurences > 1:
                start = l + 1
                while occurences > 0:
                    l += 1
                    chars.insert(l, str(occurences % 10))
                    occurences //= 10

                end = l
                while start < end:
                    chars[start], chars[end] = chars[end], chars[start]
                    start += 1
                    end -= 1

            l += 1
            r = l

        return len(chars)

