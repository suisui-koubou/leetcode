# 1483. Kth Ancestor of a Tree Node

https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/solutions/2305895/mo-ban-jiang-jie-shu-shang-bei-zeng-suan-v3rw/?envType=daily-question&envId=2024-04-06

类似**线段树**和**快速幂**的思想，任意整数 $k$ 可以分解成若干不同的2的幂。
(如 $ 13 = 8 + 4 + 1$ )

## 树上倍增算法

一个朴素的想法是可以暴力解决 (注意题目已经给出 `parent` 数组，也就是每个节点的 parent 都是唯一的，只要按照次数向上寻找)。

一步一步往上跳，就是 

$ 
node \rightarrow parent[node] \rightarrow parent[parent[node]] \rightarrow ... 
$

更快的解决是可以预处理得到 “爷爷节点”。

预处理出每个节点的第 $2^i$ 个祖先节点，即第 $1,2,4,8,\cdots$ 个祖先节点。由于任意 $k$ 可以分解为若干不同的 $2$ 的幂（例如 $13=8+4+1 = 1101_{(2)}$ ），所以只需要预处理出这些 $2^i$ 祖先节点，就可以快速地到达任意第 $k$ 个祖先节点。

```

```


## 拓展: 最近公共祖先

