# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # This will track the node before the pair we're swapping
        curr = head
        
        while curr and curr.next:
            # Identify the pair to swap
            first = curr
            second = curr.next
            
            # Perform the swap by adjusting pointers
            prev.next = second  # prev points to second
            first.next = second.next  # first points to the node after second
            second.next = first  # second points to first

            # Move the pointers forward
            prev = first  # prev now becomes the first node (after swap)
            curr = first.next  # curr moves to the next pair

        return dummy.next  # Return the new head (dummy.next)