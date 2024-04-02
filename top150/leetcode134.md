# 134. Gas Station

真的没想到还能用 “不等式” 要证明猜想。

猜想: 
> 假设 A->B ，刚好 B 的下一站是无法到达的(即最后可以到达的加油站是B)
> 那么A、B之间的所有点出发也无法到达B点的下一站。
> 也就是下一个点应该选择B点的下一站。

## 模拟 + 贪心优化

```python 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0 
        while i < n:                        # 从 i 点开始模拟 
            sumOfGas = 0
            sumOfCost = 0 
            cnt = 0                         # 可以顺时针往后模拟多少个加油站
            while cnt < n:                  # 条件1: 环绕一圈后结束
                j = (i + cnt) % n 
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfCost > sumOfGas:    # 条件2: 无法到达
                    break 
                cnt += 1 
            if cnt == n:                    # 检查是否因为条件1退出循环
                return i 
            else: 
                i = i + cnt + 1;            # 如果 i->i+cnt 无法到达下一站，那么中间的站都不用看
        return -1 
```