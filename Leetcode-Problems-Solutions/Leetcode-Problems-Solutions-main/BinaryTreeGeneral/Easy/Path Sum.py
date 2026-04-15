# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self, root: Optional[TreeNode],s: set):
        if not root:
            return
        if root.left:
            root.left.val += root.val
            self.path(root.left,s)
        if root.right:
            root.right.val += root.val
            self.path(root.right,s)
        if not root.left and not root.right:
            s.add(root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        s = set()
        self.path(root,s)
        print(s)
        return (targetSum in s) 
        
