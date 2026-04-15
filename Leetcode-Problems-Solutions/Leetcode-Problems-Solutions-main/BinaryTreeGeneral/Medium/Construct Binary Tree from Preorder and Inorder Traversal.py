# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] or inorder == []:
            return None
        res = TreeNode(preorder[0]) 
        index = inorder.index(preorder[0])
        left = inorder[:index]
        right = inorder[index+1:]
        res.left = self.buildTree(preorder[1:],left)
        res.right = self.buildTree(preorder[1+index:],right) 
        return res
