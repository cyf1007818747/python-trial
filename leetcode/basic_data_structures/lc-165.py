class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_nums = version1.split('.')
        v2_nums = version2.split('.')

        for i in range(max(len(v1_nums), len(v2_nums))):
            # case that one list out of range
            if i >= len(v2_nums):
                # you forgot to add this after adding strp1, strp2 below # *
                # the code can still run (since the code below are entered first), but contains logic error
                strp1 = v1_nums[i].lstrip('0')
                n1 = int(strp1) if strp1 != '' else 0
                if n1 == 0:
                    continue
                return 1
            elif i >= len(v1_nums):
                strp2 = v2_nums[i].lstrip('0')
                n2 = int(strp2) if strp2 != '' else 0
                if n2 == 0:
                    continue
                return -1
            
            # you do not even bother to strip, since int('0001') = 1 # *
            strp1, strp2 = v1_nums[i].lstrip('0'), v2_nums[i].lstrip('0')
            # you need to consider the special strip case: '0' or '0's are stripped to ''
            # and int('') in python generates runtime error
            # // n1 = int(v1_nums[i].lstrip('0'))
            # // n2 = int(v2_nums[i].lstrip('0'))
            n1 = int(strp1) if strp1 != '' else 0
            n2 = int(strp2) if strp2 != '' else 0
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1

        return 0
