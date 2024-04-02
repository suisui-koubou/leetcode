from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MAX_N = 11 
f = [[] for _ in range(MAX_N)]
f[1] = [TreeNode(0)]
for i in range(2, MAX_N):
    f[i] = [TreeNode(0, left, right)
            for j in range(1, i) # 枚举左子树的节点数
            for left in f[j]     # 枚举左子树
            for right in f[i-j]  # 枚举右子树
            ]

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return f[(n + 1) // 2] if n % 2 else []