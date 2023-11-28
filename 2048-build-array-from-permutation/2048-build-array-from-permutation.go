func buildArray(nums []int) []int {
    m := make(map[int]int)

    for i, v := range nums {
        m[i] = nums[v]
    }
    
    for i := range nums {
        nums[i] = m[i]
    }

    return nums
}