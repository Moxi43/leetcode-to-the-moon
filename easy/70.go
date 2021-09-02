// Link to the problem: https://leetcode.com/problems/climbing-stairs/

import "math"

func climbStairs(n int) int {
	var nf float64 = float64(n)
	res := (math.Pow(((1+math.Sqrt(5))/2), nf) - (math.Pow((1-math.Sqrt(5))/2, nf))) / math.Sqrt(5)
	var x int = int(res)
	return x + 1
}