# 2810. Faulty Keyboard

## 脑筋急转弯

动手模拟一下整个过程就会发现了。

**脑子不够，动手来凑**。

```
str
rts ng 
```

原来反转后，在数组的另一头继续写入字母也是合理的，符合的数据结构是“双端队列”。

```python
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
```
