# 45. Jump Game II

## 暴力法

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [inf] * n
        f[0] = 0
        for i in range(n):
            step_limit = i + nums[i] 
            if step_limit >= n: 
                step_limit = n - 1 
            for j in range(i+1, step_limit+1):
                f[j] = min(f[j], f[i] + 1) 
        return f[n-1]
```


## 正向查找可到达的最大位置

这是基于 Jump Game I 的想法，就是维护一个最远可达的位置。

https://leetcode.cn/problems/jump-game-ii/solutions/2652894/pythongoc-dong-tai-geng-xin-zui-yuan-ju-yqhjs/?envType=study-plan-v2&envId=top-interview-150

> 既然题目保证可以到达终点，只是统计最小的跳跃次数，其实就是55跳跃游戏的最少更新次数。
> 怎样减少更新次数呢？每次更新最远距离后，在下一个区间内找下一个最远距离，算一次更新即可。

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        curr, maxPos = 0, 0
        while maxPos < len(nums) - 1:
            nextMaxPos = maxPos                     # 需要一个初始值而已，最差的情况是没有做任何贡献。
            for opt in range(cur, maxPos + 1):      # 在步数不需要增加的情况下，计算下一个边界
                nextMaxPos = max(nextMaxPos, opt + nums[opt])
            curr, maxPos = maxPos + 1, nextMaxPos   # 开始下一个边界。
                                                    # 要注意 maxPos 以前的情况已经计算完了。从 maxPos + 1 开始。
            ans += 1
        return ans
```

还是不明白的话可以看看 LeetCode 官方题解的图示: 

<https://leetcode.cn/problems/jump-game-ii/solutions/230241/tiao-yue-you-xi-ii-by-leetcode-solution/?envType=study-plan-v2&envId=top-interview-150>

> Benhao大佬的代码总是那么易读、优雅。