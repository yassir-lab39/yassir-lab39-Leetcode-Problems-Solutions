# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = 0
        q = [root]
        l = [root.val]
        while q != []:
            for i in range(len(l)):
                a = q.pop(0)
                n = l.pop(0)*10
                if a.left:
                    q.append(a.left)
                    l.append(a.left.val+n)
                if a.right:
                    q.append(a.right)
                    l.append(a.right.val+n)
                if not a.left and not a.right:
                    s += n
        return s//10
