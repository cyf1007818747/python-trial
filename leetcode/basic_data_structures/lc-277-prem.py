# all from chatGPT since premium

"""
LeetCode Problem 277, "Find the Celebrity," revolves around identifying a "celebrity" among a group 
of people. The celebrity is defined as someone who:

Knows no other person.
Is known by everyone else.
You are given a helper function bool knows(a, b), which returns True if person a knows person b, 
otherwise False. With this function, you need to find out if there is a celebrity in the party, 
and if there is, return their index (0-indexed). If there is no celebrity, return -1.

Here's a strategy to solve this problem efficiently:

Candidate Selection: Assume the first person is a candidate for celebrity. Iterate through the people. 
For each person i, if the candidate knows i, then i could be the celebrity, so update the candidate to i. 
The intuition is that if candidate knows i, then candidate cannot be a celebrity, but i could be because 
everyone must know the celebrity, and the celebrity knows nobody. By the end of this process, 
we will have one candidate who might be the celebrity.

Verification: After identifying a candidate, verify if they are truly a celebrity by ensuring two conditions:

The candidate does not know anyone.
Everyone knows the candidate.
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a: int, b: int) -> bool:
    # some predefined function, omitted here
    return True # ! this is a fake function


class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find the candidate
        candidate = 0
        for i in range(1, n):
            """
            knows() can exactly one of the 2 argument that is impossible to be the celebrity
            for the other one, it cannot tell whether it is or not
            the code below does this:
            > if it is the candidate that is impossible to be the celebrity, we pass it by making it to be i
            > if it is i that is impossible to be the celebrity, we pass if by doing nothing (since next loop it is passed)
            for all the numbers before i, they are all checked. They are either passed by passing the loop, or 
            not passed by being stored in candidate

            Eventually, there is only one value that is POSSIBLE to be the the celebrity: candidate
            """
            if knows(candidate, i):
                candidate = i
                
        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
                
        return candidate
