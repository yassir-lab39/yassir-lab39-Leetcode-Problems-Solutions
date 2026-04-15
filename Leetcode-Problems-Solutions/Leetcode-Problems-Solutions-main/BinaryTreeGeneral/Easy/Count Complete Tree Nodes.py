# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 0
        count = 2**level
        while q != []:
            for i in range(len(q)):
                a = q.popleft()
                if a.left:
                    q.append(a.left)
                else:
                    return count + i*2
                if a.right:
                    q.append(a.right)
                else:
                    return count + i*2 + 1
            level += 1
            count += 2**level
        return count
