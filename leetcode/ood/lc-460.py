from typing import List

# the solution below is after reading .cn official solution, 2nd approach

# freq_dic: key - freq, value DE linked list, where last accessed at the first
# kv_dic: key - k, value - node
# node: key, value, freq
# get: look up kv_dic, and move node to the head of freq_dic[freq+1]
# put:
# > if not exist, insert into freq 1 de linked list
# > else update value, increase freq by 1 (by to the head of freq + 1)
# if capacacity > cap:
# -- from the min freq de list, remove tail prev, and update min_freq

# min freq de list: maintain after each increasing of of freq to freq + 1:
# > if original freq len > 0, min_freq does not change
# > else increase min_freq by 1

# passed 21/25 cases
class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.freq = 0
        self.prev = None
        self.next = None

def insert(nd: Node, new_prev: Node, new_next: Node):
    new_prev.next, nd.prev = nd, new_prev
    nd.next, new_next.prev = new_next, nd

def remove(nd: Node):
    old_prev, old_next = nd.prev, nd.next
    old_prev.next, old_next.prev = old_next, old_prev
    nd.prev, nd.next = None, None

# initialize freq_dic to be head and tail, return head
def init_de_linlist() -> List[Node]:
    head, tail = Node(), Node()
    head.next, tail.prev = tail, head
    return (head, tail)

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.freq_dic = {}
        self.kv_dic = {}

    def increase_freq(self, nd: Node):
        freq = nd.freq
        remove(nd)
        if self.freq_dic.get(freq + 1) == None:
            self.freq_dic[freq + 1] = init_de_linlist()
        head, tail = self.freq_dic[freq+1]
        insert(nd, head, head.next)
        # update min freq wje nd.freq has no element
        if self.freq_dic[freq][0].next is self.freq_dic[freq][1]:
            self.min_freq = freq + 1
        nd.freq += 1

    def get(self, key: int) -> int:
        # deal with self.cap = 0
        if self.cap == 0:
            return -1

        if key not in self.kv_dic:
            return -1
        else:
            nd = self.kv_dic[key]
            self.increase_freq(nd)
            return nd.val

    def put(self, key: int, value: int) -> None:
        # deal with self.cap = 0
        if self.cap == 0:
            return
    
        if key in self.kv_dic:
            nd = self.kv_dic[key]
            nd.val = value
            self.increase_freq(nd)
        else:
            # check capacity
            if len(self.kv_dic) == self.cap:
                hd, tl = self.freq_dic[self.min_freq]
                tl_prev = tl.prev
                remove(tl_prev)
                self.kv_dic.pop(tl_prev.key)

            nd = Node(key, value)
            nd.freq = 1
            self.kv_dic[key] = nd
            if self.freq_dic.get(1) == None:
                self.freq_dic[1] = init_de_linlist()
            head, tail = self.freq_dic[1]
            insert(nd, head, head.next)
            self.min_freq = 1
