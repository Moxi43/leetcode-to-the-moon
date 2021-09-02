# Link to the problem: https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        
        slow = head
        fast = head.next
        
        while fast:
            if fast.val==val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        
        if head.val == val:
            return head.next
        return head
            
    