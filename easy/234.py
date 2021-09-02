# Link to the problem: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        reversed_list = None
        
        while fast is not None and fast.next is not None:
            tmp = slow
            
            slow = slow.next
            fast = fast.next.next
            
            tmp.next = reversed_list
            reversed_list = tmp
        
        if fast is not None:
            slow = slow.next
        
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next
        return reversed_list is None
            
            
        