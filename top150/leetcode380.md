# 380. Insert Delete GetRandom O(1)

## 我的尝试

容易想到 `insert` 和 `remove` 操作是比较简单的，用一个 Hash维护就可以了。

思路: 
- 思路1: 
  - 如果 `getRandom` 不是 $O(1)$ 也比较容易实现，就是 Rejection Samping 就可以了。
- 思路2: 
  - 假设现在只有 `insert` 和 `getRandom`, 那就非常简单。
  - 这就是意味着我们只需要对 `remove` 特殊处理就可以。
  - 可以想到如果删除的时候，用数组末尾填充产生的空洞即可。


```python
import random 

class RandomizedSet:

    def __init__(self):
        self.dlist = []
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashMap: 
            return False
        self.hashMap[val] = len(self.dlist)
        self.dlist.append(val)  
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap: 
            return False
        slotIdx = self.hashMap.pop(val)
        tailVal = self.dlist[-1]
        self.dlist[slotIdx] = tailVal
        self.hashMap[tailVal] = slotIdx
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.dlist)-1)
        return self.dlist[idx] 
```

还是不对，但非常接近了。

```
["RandomizedSet","insert","remove","insert"]
[[],[0],[0],[0]]


输出 [null,true,true,false]
预期 [null,true,true,true]
```

所以这里可以得到一个提示: 

> "替换" 和 "删除" 操作最好分开进行。
> 在替换完成之后，再删除，就可以避免讨论 `n=1` 的情况。


```python 
import random 

class RandomizedSet:

    def __init__(self):
        self.dlist = []
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashMap: 
            return False
        self.hashMap[val] = len(self.dlist)
        self.dlist.append(val)  
        return True


    def remove(self, val: int) -> bool:
        if val not in self.hashMap: 
            return False
        slotIdx = self.hashMap[val]
        tailVal = self.dlist[-1]
        self.dlist[slotIdx] = tailVal
        self.hashMap[tailVal] = slotIdx
        self.dlist.pop()
        self.hashMap.pop(val)
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.dlist)-1)
        return self.dlist[idx] 
```
