# Link to the problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast:
            if slow.val == fast.val: 
                slow.next = slow.next.next 
            else:
                slow = fast 
            fast = fast.next
        return head 
        
            
            