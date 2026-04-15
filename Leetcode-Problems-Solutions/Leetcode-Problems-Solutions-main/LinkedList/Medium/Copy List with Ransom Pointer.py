# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None
        if not head.next :
            a = Node(head.val)
            if head.random :
                a.random = a
            return a
        current = head
        l = []
        random_index = dict()
        while current :
            l.append(Node(current.val))
            if len(l) >= 2 :
                l[-2].next = l[-1]
            current = current.next
        current = head
        index = 0
        while current :
            random_index[current] = index
            index += 1
            current = current.next
        current = head
        for i in range(len(l)) :
            if current.random :
                l[i].random = l[random_index[current.random]]
            current = current.next
        return l[0]
        
        
