# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head 
        reached = False
        l1,l2,l3 = [],[],[]
        while current :
            if current.val < x :
                l1.append(current.val)
            if current.val > x and not reached:
                l3.append(current.val)
            if current.val >= x and reached:
                l2.append(current.val)
            if current.val == x and not reached :
                reached = True
                l3.append(current.val)
            current = current.next         
        l1 = l1 + l3
        left = ListNode(-1)
        right = ListNode(-1)
        current_left = left
        current_right = right
        for i in range(len(l1)) :
            current_left.next = ListNode(l1[i])
            current_left = current_left.next
        for i in range(len(l2)) :
            current_right.next = ListNode(l2[i])
            current_right = current_right.next
        right = right.next
        current_left.next = right
        return left.next
    



        
