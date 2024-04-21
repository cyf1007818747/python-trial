from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use a dummy head dhead
# init lastsorted to be head, and for element cur behind lastsorted
# > if cur.val >= lastsorted val, proceed lastsorted and cur
# > else remove cur, iterate over dhead to lastsorted, and insert if cur val >= prev and < next
# // proceed lastsorted until lastsorted.next is None
# only proceed lastsorted if cur's position is not changed
# start to AC - 28:37
# AC
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead = ListNode(val=-5001, next=head)
        lastsorted = head
        
        while lastsorted and lastsorted.next:
            cur = lastsorted.next
            if cur.val < lastsorted.val:
                # remove cur
                lastsorted.next = cur.next
                # insert into correct place before lastsorted
                ptr = dhead
                while ptr != lastsorted:
                    if ptr.val <= cur.val and ptr.next.val >= cur.val:
                        cur.next = ptr.next
                        ptr.next = cur
                        break
                    ptr = ptr.next
            # logic error: only proceed lastsorted if cur's position is not changed # *
            # otherwise you will skip inserting some nodes
            # // lastsorted = lastsorted.next
            else:
                lastsorted = lastsorted.next

        return dhead.next


# improve code style of solution 1
class Solution2:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead = ListNode(val=-5001, next=head)
        lastsorted = head
        
        while lastsorted and lastsorted.next:
            cur = lastsorted.next
            if cur.val >= lastsorted.val:
                lastsorted = lastsorted.next
                continue
            # remove cur
            lastsorted.next = cur.next
            # insert into correct place before lastsorted
            ptr = dhead
            while not (ptr.val <= cur.val <= ptr.next.val):
                ptr = ptr.next
            cur.next = ptr.next
            ptr.next = cur

        return dhead.next
