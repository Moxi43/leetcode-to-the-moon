// Link to the problem: https://leetcode.com/problems/sqrtx/

func mySqrt(x int) int {
    l, r := 0, x
    for l <= r {
        mid := l + (r-l)/2
        if mid*mid <= x && x < (mid+1)*(mid+1) {
            return mid
        } else if x < mid*mid {
            r = mid - 1
        } else {
            l = mid+1
        }
    }
    return 0
}
