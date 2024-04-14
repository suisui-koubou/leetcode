# Design HashSet 

```python
BASE = 769 

class MyHashSet:

    def __init__(self):
        self.data = [deque() for _ in range(BASE)]
        
    def hash(self, key: int) -> int: 
        return key % BASE 

    def add(self, key: int) -> None:
        if not self.contains(key):
            h = self.hash(key)
            self.data[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        try:
            self.data[h].remove(key)
        except: 
            return

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        for e in self.data[h]: 
            if e == key: 
                return True 
        return False 
```