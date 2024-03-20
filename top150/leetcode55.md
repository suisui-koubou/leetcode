# 55. Jump Game

## Brute Force 

```python 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # next_i = (i, i + nums[i])
        n = len(nums)
        f = [False] * (n + 1)
        f[0] = True
        for i in range(0, n):
            next_i = i + nums[i]
            for j in range(i+1, min(next_i, n)+1):
                f[j] = f[i]
        return f[n-1]
```

## 类马尔可夫链/贪心

在脑子里模拟跳的过程时，突然想到只要记录当前最远的距离就可以了。

```python 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0 
        curr_reachable = 0
        while i < n: 
            if i <= curr_reachable:
                curr_reachable = max(curr_reachable, i + nums[i])
            i += 1 
        return curr_reachable >= n-1
```
