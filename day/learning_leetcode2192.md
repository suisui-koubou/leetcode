# 2192. All Ancestors of a Node in a Directed Acyclic Graph


## 逆向思维/等义转换 + BFS/DFS

- 假设 A 是 B 的 ancestor, 即 A->B 。
- 反着追踪 B 的 ancestor 其实难一点，不好写 DFS/BFS。
  - 一般 DFS 只知道自己的子节点，追踪父节点需要额外的数据结构。
  - 但是求祖先的问题把方向变一下就是求子孙的问题。
- 但是如果求经过的点就很容易

```python 
class Solution:  
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[1]].append(e[0])
        ans = [[] for _ in range(n)]
        
        def dfs(curr: int, x: int, vis: List[bool]):
            for nx in g[x]:
                if not vis[nx]:
                    vis[nx] = True
                    ans[curr].append(nx)
                    dfs(curr, nx, vis)
        
        for i in range(n):
            dfs(i, i, [False] * n) # the ancestors of i if starting from i 
            ans[i].sort()

        return ans
```


## 拓扑排序

- 如果我们**从入度为零的节点开始**呢?
- 我们是不是可以保证**由浅到深**遍历 Directed Acyclic Graph ?
- 如果是这样的话，我们在计算更深的节点时，是不是可以直接 append 之前算过的点的答案？

