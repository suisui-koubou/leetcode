


## DFS 
```python 
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, node_cloned: TreeNode)->TreeNode:
            if node == None: 
                return None
            if node == target:
                return node_cloned
            left_ans = dfs(node.left, node_cloned.left) if node.left else None
            if left_ans: 
                return left_ans
            right_ans = dfs(node.right, node_cloned.right) if node.right else None
            if right_ans: 
                return right_ans
            return None
        return dfs(original, cloned)
```


注意到可以简化条件的

```python 
w
```