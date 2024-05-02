
# start to AC - 7:32
# AC
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        left_btk = ["(", "{", "["]
        right_btk = {
            ")": 0,
            "}": 1,
            "]": 2
        }

        for c in s:
            if c in left_btk:
                stk.append(c)
            elif c in right_btk:
                matching_left = left_btk[right_btk[c]]
                # edge cases !!
                # // if stk[-1] == matching_left:
                if stk and stk[-1] == matching_left:
                    stk.pop()
                else:
                    return False
            else:
                raise Exception('error: wrong input')

        return len(stk) == 0
