"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        l = [root]
        while l != []:
            n = len(l)
            for i in range(n):
                a = l.pop(0)
                if i != n-1:
                    a.next = l[0]
                if a.left:
                    l.append(a.left)
                if a.right:
                    l.append(a.right)
        return root
            


        
