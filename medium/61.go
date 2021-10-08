// Link to the problem: https://leetcode.com/problems/rotate-list/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {

    if head == nil { return nil }

    lastElement := head
    length := 1

    for lastElement.Next != nil {
        lastElement = lastElement.Next
        length += 1
    }

    k %= length

    lastElement.Next = head

    tempNode := head

    for i:=0; i < length-k-1; i++ {
        tempNode = tempNode.Next
    }

    res := tempNode.Next

    tempNode.Next = nil

    return res
}
