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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedValues = self.sortedValues(root)
        return sortedValues[k-1]
