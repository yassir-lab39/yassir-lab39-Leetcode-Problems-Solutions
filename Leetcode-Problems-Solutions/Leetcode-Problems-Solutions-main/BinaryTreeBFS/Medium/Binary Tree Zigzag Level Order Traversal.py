# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l = [root]
        res = [[root.val]]
        leftToRight = False
        while l != [] :
            n = len(l)
            for i in range(n):
                a = l.pop(0)
                if a.left:
                    l.append(a.left)
                if a.right:
                    l.append(a.right)
            if l != []:
                L = []
                if leftToRight:
                    for n in l:
                        L.append(n.val)
                if not leftToRight:
                    for i in range(len(l)-1,-1,-1):
                        L.append(l[i].val)
                res.append(L)
            leftToRight = not leftToRight
        return res
