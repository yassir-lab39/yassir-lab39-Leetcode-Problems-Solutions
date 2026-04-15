# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        l = [root]
        res = [root.val]
        while l != [] :
            s = 0
            n = len(l)
            for i in range(n):
                a = l.pop(0)
                if a.left:
                    l.append(a.left)
                if a.right:
                    l.append(a.right)
            if l != []:
                for i in range(len(l)):
                    s += l[i].val
                res.append(s/len(l))
        return res
