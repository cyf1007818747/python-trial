import bisect

# start to AC - 13:22
# AC
class MyCalendar:
    def __init__(self):
        self.sorted_keys = []
        self.dic = {} # key: start, value: end

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.sorted_keys, end)
        if idx > 0:
            pre_start = self.sorted_keys[idx - 1]
            if self.dic[pre_start] > start:
                return False
        # you initially only return True when idx == 0, but forgot to insert - silly error !! # *
        bisect.insort_left(self.sorted_keys, start)
        self.dic[start] = end
        return True
