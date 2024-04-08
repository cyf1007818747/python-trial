# ""
# (
# )
# (*))
class Solution:
    def checkValidString(self, s: str) -> bool:
        stk_lb = []
        stk_star = []

        # iterate over s
        # > for ( or *, push their index in corresponding stacks
        # for ), try to match (, else match *, if neither can be matched, return false
        for i in range(len(s)):
            # // if s == "("
            if s[i] == "(":
                stk_lb.append(i)
            # // if s == "("
            elif s[i] == "*":
                stk_star.append(i)
            else:
                if stk_lb:
                    stk_lb.pop()
                elif stk_star:
                    # stk_lb.star() # * ??
                    stk_star.pop()
                else:
                    return False

        # for the remaining ( and *, while they are both not None:
        # > if len ( > len *, return False
        # > else pop ( and * one by one, continue matching
        # >> if index ( is smaller than index *, pop them continue matching
        # >> if there is a ('s index > *'s index, return False
        while stk_lb and stk_star:
            if len(stk_lb) > len(stk_star):
                return False
            lb = stk_lb.pop()
            star = stk_star.pop()
            if lb >= star:
                return False

        # finally, if ( stack is empty, return True, else false
        return False if stk_lb else True
