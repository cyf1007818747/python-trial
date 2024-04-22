import random

# use both list and dict in python, after seeing .cn solution
# start to AC - 20:32 (8 minutes used to debug the error of 2 lines below)
# AC
class RandomizedSet:
    def __init__(self):
        self.lis = []
        self.dic = {}


    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.lis.append(val)
        self.dic[val] = len(self.lis) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        idx = self.dic[val]
        self.dic.pop(val)
        # if having these 2 lines without the condition below,
        # the removed element will be added back to the list
        # // self.lis[idx] = self.lis[-1]
        # // self.dic[self.lis[-1]] = idx
        if idx != len(self.lis) - 1:
            self.lis[idx] = self.lis[-1]
            self.dic[self.lis[-1]] = idx
        self.lis.pop()
        return True
    

    def getRandom(self) -> int:
        return random.choice(self.lis)
