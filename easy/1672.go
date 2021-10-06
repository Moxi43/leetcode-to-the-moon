// Link to the problem: https://leetcode.com/problems/richest-customer-wealth

func maximumWealth(accounts [][]int) int {
    max_val := 0
    for _, acc := range accounts {
        max_val = maxInt(max_val, sumArr(acc))
    }
    return max_val
}

func maxInt(x int, y int) int {
    if y > x { return y }
    return x
}

func sumArr(arr []int) int {
    sum := 0
    for _, val := range arr {
        sum += val
    }
    return sum
}
