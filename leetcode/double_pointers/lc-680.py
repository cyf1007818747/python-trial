
# Initial solution
# !! time limit exceeded at Leetcode
# but 394 / 471 cases passed so should be functionally correct
def validPalindromeInitial(s: str) -> bool:
    # > case of short s:
    if len(s) <= 2:
        return True
    
    # > check whether deleting 0 char makes it palidrome
    l, r = 0, len(s) - 1
    self_palindrome = True
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        # > else casel :: is not palidrome
        else:
            self_palindrome = False
            break
    
    # early return s itself is palidrome
    if self_palindrome:
        return True
    
    # print("---- finished checking self palindrome")

    # > check whether deleting 1 char makes it palidrome
    for i in range(0, len(s)):
        l, r = 0, len(s) - 1
        palindrome = True
        # print("deleting index {}".format(i))
        while l < r:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            # print("---- checking char {} and char {}".format(s[l], s[r]))
            if s[l] == s[r]:
                l += 1
                r -= 1
            # > else casel :: is not palidrome
            else:
                palindrome = False
                break
        if palindrome:
            return True

    return False

# passed all tests on leetcode
def validPalindrome_O_n(s: str) -> bool:
    # > case of short s of len <= 2:
    if len(s) <= 2:
        return True
    
    # > else :: len(s) >= 2
    l, r = 0, len(s) - 1
    while l < r:
        # >> 2 chars are equal
        if s[l] == s[r]:
            l += 1
            r -= 1
        # >> else :: 2 chars are not equal
        else:
            break

    # if s[l] != s[r], you have to delete one of them
        
    # >> try delete s[l]
    ll, rr = l + 1, r
    palidromeNoL = True
    while ll < rr:
        if s[ll] == s[rr]:
            ll += 1
            rr -= 1
        else:
            palidromeNoL = False
            break
    if palidromeNoL:
        return True
    
    # >> try delete s[r]
    ll, rr = l, r - 1
    palidromeNoR = True
    while ll < rr:
        if s[ll] == s[rr]:
            ll += 1
            rr -= 1
        else:
            # palidromeNoR = False
            # break
            # can directly return false here, since both deleting L or R does not work
            return False
    if palidromeNoR:
        return True
    
    # the case when deleting both does not work
    return False


def validPalindrome_O_n_helperFunc(s: str) -> bool:
    # start >= 0, end <= len(s) - 1
    def checkPalidrome(start: int, end: int) -> (bool, int, int):
        if len(s) <= 1:
            return True
        
        l, r = start, end
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False, l, r
            
        return True, l, r
    
    isPalidrome, l, r = checkPalidrome(0, len(s) - 1)

    # > s itself is palindrome
    if isPalidrome:
        return True
    
    # > s itself is not palindrome
    
    # >> try delete s[l]
    isPalidromeNoL, _, _ = checkPalidrome(l + 1, r)
    if isPalidromeNoL:
        return True
    
    # >> since deleting s[l] does not work, return whether deleting s[r] works
    return checkPalidrome(l, r - 1)[0]



testString = "eccer"
output = validPalindrome_O_n_helperFunc(testString)
print("#### output: {}".format(output))
    