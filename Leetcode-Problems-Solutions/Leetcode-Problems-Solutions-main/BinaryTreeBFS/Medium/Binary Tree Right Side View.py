# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = [root]
        res = [root.val]
        while l != [] :
            n = len(l)
            for i in range(n):
                a = l.pop(0)
                if a.left:
                    l.append(a.left)
                if a.right:
                    l.append(a.right)
            if l != []:
                res.append(l[-1].val)
        return res
