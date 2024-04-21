"""
Question: Design Hashmap
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None

# use buckets and linked list (after reading .cn solution)
# start to AC - 6:34
# AC
class MyHashMap:
    def __init__(self):
        self.buckets = [ None for _ in range(1009)]

    def put(self, key: int, value: int) -> None:
        buc_id = key % 1009
        if not self.buckets[buc_id]:
            self.buckets[buc_id] = ListNode(key, value)
        else:
            # search existing keys
            cur = self.buckets[buc_id]
            while cur.next:
                # // if cur.key = key:
                if cur.key == key:
                    cur.val = value
                    return
                cur = cur.next
            if cur.key == key:
                cur.val = value
                return
            else:
                cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        buc_id = key % 1009
        if self.buckets[buc_id] == None:
            return -1

        cur = self.buckets[buc_id]
        while cur:
            if cur.key == key:
                # // return cur.value
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        buc_id = key % 1009
        if self.buckets[buc_id] == None:
            return
        
        cur = self.buckets[buc_id]
        # remove 1st element
        if cur.key == key:
            self.buckets[buc_id] = cur.next
            return
        # remove later elements or do nothing
        pre = cur
        cur = cur.next
        while cur:
            if cur.key == key:
                pre.next = cur.next
            pre = cur
            cur = cur.next
