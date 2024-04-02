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

