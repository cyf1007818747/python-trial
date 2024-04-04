# All solutions for this question were written after reading the official .cn solution

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# use Python built in ordered dict structure (simplest)
# initial solution
# AC
from collections import OrderedDict, deque

class LRUCache(OrderedDict): # *
    def __init__(self, capacity: int):
        # // super.__init__()
        super().__init__()
        self.cap = capacity

    def get(self, key: int) -> int:
        # since the above get will overwrite the default get,
        # you cannot use get in the way below # *
        # // if not self.get(key):
        if not key in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        # the same reason as above
        # //if self.get(key):
        if key in self:
            self[key] = value
            self.move_to_end(key)
            return

        self[key] = value
        self.move_to_end(key)
        # // if len(self) > cap:
        if len(self) > self.cap:
            # // self.popitem()
            self.popitem()

        # this return is not necessary, but it is fine if you leave it
        # // return

# use python deque data structure
class LRUCache2:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = dict()
        self.dq = deque()


    def get(self, key: int) -> int:
        # you make this error again !! this is because value 0 evaluates to False # *
        # // if not self.dic.get(key):

        # logic error !! also, do not use 'is'. Use '=='. # *
        # // if not self.dic.get(key) is None:
        if self.dic.get(key) is None:
            return -1

        self.dq.remove(key)
        self.dq.append(key)
        
        # // return self.dic(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        # You made this mistake again !!!!!!!!!! # *
        # // if self.dic.get(key):
        if self.dic.get(key) != None:
            self.dic[key] = value
            # // dq.remove(key)
            # // dq.append(key)
            self.dq.remove(key)
            self.dq.append(key)
            return

        # add new k v pair
        self.dic[key] = value
        self.dq.append(key)
        # // if len(dq) > self.cap:
        if len(self.dq) > self.cap:
            key_removed = self.dq.popleft()
            self.dic.pop(key_removed)  # this is very important and you forget it first # *


# use a self created double ended linked list
# use double ended linked list
# start to AC - 34:00
# AC
class LRUCache3:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = dict()
        self.head = DEListNode()
        self.tail = DEListNode()
        self.head.next = self.tail
        self.tail.prev = self.head # you initially forgot # *

    def get(self, key: int) -> int:
        if self.dic.get(key) == None:
            return -1
        
        node = self.dic[key]
        
        # you initially correct the code in put() but forgot to correct here # *
        # the 3 lines of code below are very easy to make mistakes # *
        # remove node from initial position
        node.prev.next, node.next.prev = node.next, node.prev
        # insert node to the front
        node.next, self.head.next.prev  = self.head.next, node
        self.head.next, node.prev = node, self.head

        return node.value


    def put(self, key: int, value: int) -> None:
        # update existing k v pair
        if self.dic.get(key) != None:
            node = self.dic[key]
            node.value = value
            # remove node from initial position
            node.prev.next, node.next.prev = node.next, node.prev
            # insert node to the front
            node.next, self.head.next.prev  = self.head.next, node
            self.head.next, node.prev = node, self.head
            return

        # add new k v pair
        node = DEListNode(key, value)
        self.dic[key] = node
        # add node to head
        node.next, self.head.next.prev  = self.head.next, node
        self.head.next, node.prev = node, self.head
        # check for capcacity
        if len(self.dic) > self.cap:
            lastNode = self.tail.prev
            # // lastNode.prev.next, self.tail.prev = tail, lastNode.prev
            lastNode.prev.next, self.tail.prev = self.tail, lastNode.prev
            # // self.dic.popitem(lastNode.key)
            self.dic.pop(lastNode.key)

class DEListNode:
    def __init__(self, key = 0, value: int = 0): # initially no key
        self.key = key # initially not added
        self.value = value
        self.prev = None
        self.next = None


# write deque solution again, but should be quicker this time
# start to AC - 6:48
# AC
# good !! you only made 1 mistake: wrote popitem instead of remove, which is an API error due to no reference
class LRUCache4:
    from collections import deque
    def __init__(self, capacity: int):
        self.dic = dict()
        self.dq = deque()
        self.cap = capacity

    def get(self, key: int) -> int:
        if self.dic.get(key) == None:
            return -1

        self.dq.remove(key)
        self.dq.append(key)

        return self.dic[key]


    def put(self, key: int, value: int) -> None:
        if self.dic.get(key) != None:
            self.dic[key] = value
            self.dq.remove(key)
            self.dq.append(key)
            return
        
        # add a new k v pair
        self.dic[key] = value
        self.dq.append(key)
        if len(self.dq) > self.cap:
            key_to_rm = self.dq.popleft()
            self.dic.pop(key_to_rm)
        