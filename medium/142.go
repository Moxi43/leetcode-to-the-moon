// Link to the problem: https://leetcode.com/problems/linked-list-cycle-ii/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    is_cycle, fast := hasCycle(head)
    if is_cycle == true {
        for head != fast {
            head = head.Next
            fast = fast.Next
        }
        return head
    }
    return nil
}

func hasCycle(head *ListNode) (bool, *ListNode) {
    slow := head
    fast := head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast {
            return true, slow
        }
    }
    return false, slow
}
