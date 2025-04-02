# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        dummy = ListNode(0, head)
        prev = dummy
        first = prev.next
        second = first.next
        # print(prev.val,first.val, second.val)
        
        while first and second:
            third = second.next
            second.next = first
            first.next = third
            prev.next = second

            prev = first
            first = third
            if first: # if first is not none
                second = first.next    
        return dummy.next