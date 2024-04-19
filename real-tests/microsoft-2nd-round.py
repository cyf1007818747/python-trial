# Implement a service which exposes the following APIs:

# insertWord() - String input, return void
# getCount() - String input, return count of the string in the last 5 minutes

import time

class Strs:
    def __init__(self):
        self.dic = {}
        self.time = time.time()
        # self.last_clear_time = 

    
    def insertWord(self, st):
        now = time.time()
        if self.dic.get(st) != None:
            self.dic[st].append(now)
        else:
            self.dic[st] = [now]
        
        # this loop can be optimized to break earlier: if encounter a time within 5 minutes, break
        # this is due to your not deep understand of the question and solution # *
        for tm in self.dic[st]:
            if now - tm > 60*5:
                self.dic[st].remove(tm)


    def getCount(self, st):
        if self.dic.get(st) == None:
            return 0
        
        now = time.time()
        count = 0
        # this loop can be optimized to break earlier: if encounter a time within 5 minutes, break
        # this is due to your not deep understand of the question and solution # *
        for tm in self.dic[st]:
            if now - tm > 60*5:
                self.dic[st].remove(tm)
            else:
                count += 1
        
        return count
