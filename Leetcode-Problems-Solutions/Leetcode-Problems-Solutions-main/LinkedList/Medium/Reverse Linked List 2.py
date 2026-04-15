# Definition for singly-linked list.
#class ListNode:
 #   def __init__(self, val=0, next=None):
  #      self.val = val
   #     self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right :
            return head
        if left == 1 and right == 2 :
            head.val, head.next.val = head.next.val, head.val
            return head
        current = head
        l = []
        i = 1
        right_side = None
        while current :
            if i >= left and i <= right :
                l.append(ListNode(current.val))
            if len(l) >= 2 :
                l[-1].next = l[-2]
            if i == right+1 :
                right_side = current
                break
            current = current.next
            i += 1
        current = l[-1]
        i = 1
        while i <= right-left :
            current = current.next
            i += 1
        current.next = right_side
        i = 1
        if left != 1 :
            current = head
            while i < left-1 :
                current = current.next
                i += 1
            current.next = l[-1]
        else :
            head = l[-1]
        return head
