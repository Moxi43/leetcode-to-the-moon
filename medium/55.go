// Link to the problem: https://leetcode.com/problems/jump-game/

func canJump(nums []int) bool {
    n := len(nums)

    if n == 1 { return true }

    max_reachable := nums[0]
    reachable := 0
    i := 1

    for i<n-1 && i <= max_reachable {
        reachable = i + nums[i]
        max_reachable = max(max_reachable, reachable)
        i += 1
    }

    if max_reachable < n-1 { return false }

    return true
}

func max(x int, y int) int {
    if y > x { return y }
    return x
}
