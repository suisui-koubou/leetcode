# 274. H-Index

https://leetcode.cn/problems/h-index/solutions/2652908/pythongoc-ji-shu-by-himymben-2wgh/?envType=study-plan-v2&envId=top-interview-150

> 排序固然简单，但没有价值。
> 二分答案也是一个选择（毕竟答案具备二分性质），
> 不过更好的是从三叶那学习O(n)的方法，统计计数后从大到小遍历（类似前缀和），找到第一个满足条件的即为答案


## 排序

> The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

可以看看灵神的答案，由题意可知 h 的最大值为 n (不可能超过 paper的数量)。

明白这一点就非常简单，我们可以从小枚举h。

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = 0 
        for h in range(0, n+1):
            c = 0
            for i in range(n):
                if citations[i] >= h: 
                    c += 1 
            if c >= h: 
                ans = max(ans, h)
        return ans
```

但是要注意到，我们真的需要全部遍历吗？

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse = True)
        h = 0
        i = 0 
        n = len(citations)
        while i < n and sorted_citation[i] > h: 
            i += 1 
            h += 1 
        return h
```

我们排序就好，**看看 Paper 的引用数是否可以让 `h` 增大。**
(按照增大后的条件是 `h + 1 >= nums[i]`, 即 `h > nums[i]`) 

直到找到一个不符合的为止。

时间复杂度 $O(nlogn)$

空间复杂度 $O(1)$


## 二分法

时间复杂度 $O(nlogn)$

空间复杂度 

## 计数排序

时间复杂度 $O(nlogn)$

空间复杂度

