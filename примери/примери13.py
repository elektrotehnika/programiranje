# -*- coding: utf-8 -*-
"""
Пример 1 - Дефинициjа класе за чвор уланчане листе.
"""
"""
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(8)

print(head.next.next.val)
"""


"""
Пример 2 - За дат почетак повезане листе и целоброjну вредност, избацити све
чворове из листе коjи имаjу ту целоброjну вредност, и вратити нови
почетак листе.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
def removeElements(head, val):
    dummy = ListNode(float('inf'), next=head)
        
    prev = dummy
    curr = head
        
    while curr:
        if curr.val == val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
                
    newHead = dummy.next
    return newHead
        
        
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(8)

newHead = removeElements(head, 4)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next.val)
