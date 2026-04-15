# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder == [] or postorder == [] :
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        left = inorder[:index]
        right = inorder[index+1:]
        root.left = self.buildTree(left,postorder[:len(postorder)-len(right)-1])
        root.right = self.buildTree(right,postorder[:len(postorder)-1])
        return root
