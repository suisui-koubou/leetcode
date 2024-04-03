

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(node: TreeNode, node_cloned: TreeNode)->TreeNode:
            if node == None: 
                return None
            if node == target:
                return node_cloned
            left_ans = dfs(node.left, node_cloned.left) if node.left else None
            if left_ans: return left_ans
            right_ans = dfs(node.right, node_cloned.right) if node.right else None
            if right_ans: return right_ans
            return None
        return dfs(original, cloned)