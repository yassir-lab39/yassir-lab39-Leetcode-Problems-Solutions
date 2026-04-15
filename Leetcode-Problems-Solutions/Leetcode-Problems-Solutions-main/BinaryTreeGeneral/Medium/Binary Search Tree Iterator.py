# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.lst = self.inorder(root)

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        traverse(root)
        return res

    def next(self) -> int:
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        return ( len(self.lst) > 0 )
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
