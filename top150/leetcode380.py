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
        self.dlist.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.dlist)-1)
        return self.dlist[idx] 




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()