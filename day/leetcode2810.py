from collections import deque
from enum import Enum

class Solution:
    def finalString(self, s: str) -> str:
        q = deque() 
        head = False
        for c in s: 
            if c == 'i':
                head = not head
            else:
                if head:
                    q.appendleft(c)
                else:
                    q.append(c)
        ans = ''.join(q)
        return ans[::-1] if head else ans 
        