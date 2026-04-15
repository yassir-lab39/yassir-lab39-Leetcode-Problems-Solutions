# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def parent(self, root : 'TreeNode', D : dict):
        if root :
            if root.left:
                D[root.left] = root
                self.parent(root.left, D)
            if root.right:
                D[root.right] = root
                self.parent(root.right, D)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = dict()
        self.parent(root, parents)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents.get(p)
        while q:
            if q in ancestors:
                return q
            q = parents.get(q)

