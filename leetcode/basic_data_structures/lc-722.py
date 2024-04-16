import re
from typing import List

# use regex, after seeing .cn solution
# start to AC - 4:59
# AC
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = '\n'.join(source)
        s = re.sub('//.*|/\*(.|\n)*?\*/', '', s)
        # recall the diff of split() and split(' ')
        # // return s.split('\n')
        # details !!
        # // return [for elem in s.split('\n') if elem]
        return [elem for elem in s.split('\n') if elem]
