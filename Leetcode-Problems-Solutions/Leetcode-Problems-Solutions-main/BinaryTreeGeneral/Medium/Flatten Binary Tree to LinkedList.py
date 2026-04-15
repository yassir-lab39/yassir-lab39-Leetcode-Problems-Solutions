# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,res: List[int], root: Optional[TreeNode]):
        if not root:
            return
        res.append(root.val)
        self.preorder(res,root.left)
        self.preorder(res,root.right)
        return res


    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root :
            return
        res = self.preorder([],root)
        if len(res) > 1:
            current = root
            current.left = None
            for i in range(1,len(res)):
                current.right = TreeNode(res[i])
                current = current.right


        
