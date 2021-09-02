# Link to the problem: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorted_list = ListNode()
        head = sorted_list
        while l1 and l2:
            if l1.val < l2.val:
                sorted_list.next = l1
                l1 = l1.next
            else:
                sorted_list.next = l2
                l2 = l2.next
            sorted_list = sorted_list.next
            
        if not l1:
            sorted_list.next = l2
        else:
            sorted_list.next = l1
        
        return head.next