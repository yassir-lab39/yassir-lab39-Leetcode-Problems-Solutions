# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedValues(self, root: Optional[TreeNode]):
        if not root:
            return []
        return self.sortedValues(root.left) + [root.val] + self.sortedValues(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sortedValues = self.sortedValues(root)
        v = sortedValues[0]
        for i in range(1,len(sortedValues)):
            if v < sortedValues[i]:
                v = sortedValues[i]
            else:
                return False
        return True
