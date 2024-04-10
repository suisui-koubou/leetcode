

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -inf

    def dfs(self, root: Optional[TreeNode]) -> List[int]:
            left_ans = []   
            right_ans = []  
            minAns = root.val
            maxAns = root.val
            if root.left: 
                left_ans = self.dfs(root.left) 
                minAns = min(minAns, min(left_ans))
                maxAns = max(maxAns, max(left_ans))
                self.res = max(self.res, abs(root.val - left_ans[0]), abs(root.val - left_ans[1]))
            if root.right: 
                right_ans = self.dfs(root.right)
                minAns = min(minAns, min(right_ans))
                maxAns = max(maxAns, max(right_ans))
                self.res = max(self.res, abs(root.val - right_ans[0]), abs(root.val - right_ans[1]))
            return [minAns, maxAns] 

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        children = self.dfs(root)
        return max(self.res, max(abs(root.val - children[0]), abs(root.val - children[1])))
```