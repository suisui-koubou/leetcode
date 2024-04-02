# 894. All Possible Full Binary Trees

## DFS 

> **注意**: 这里有一个思维误区，如果只是验证答案的话，不需要深度复制。也就是重复使用子树是可以的。

- 完全二叉树的节点数一定是奇数 (因为只能成对添加，也就是 $n+2$, 而初始值 $n=1$)。
- 函数 allPossibleFBT 可以直接跳过偶数
- 假设左子树的节点数是`i`, 右子树的节点数是`n-i-1`
- 在枚举`i`的时候注意要只列举奇数(节点成对增加)
  - 调用 allPossibleFBT 枚举所有子树
  - 利用子树的答案列表直接复用已生成的子树(这点比较难)

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        ans = []
        if n == 1: 
            ans.append(TreeNode(0))
            return ans 
        if n % 2 == 0: 
            return ans 
        for i in range(1, n, 2): # 左子树最少1个节点，最多n-1个节点(除去root)
            left_subtrees = self.allPossibleFBT(i)
            right_subtrees = self.allPossibleFBT(n - i - 1)
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(0, left, right)
                    ans.append(root)
        return ans 
```

