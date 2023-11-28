impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut new_vector : Vec<i32> = Vec::new();
        for n in 0..nums.len() {
            let v: i32 = nums[n];
            new_vector.push(nums[v as usize] as i32);
        }
        new_vector
    }
}