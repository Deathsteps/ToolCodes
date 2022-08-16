# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/

# /**
#  * @param {number[]} nums
#  * @return {number[]}
#  */
# var singleNumbers = function(nums) {
#     let n = nums.length;
#     let x = 0;
#     for (let i = 0; i < n; i ++) {
#         x ^= nums[i];
#     }
#     let mask = 1;
#     while (!(x & mask)) {
#         mask <<= 1;
#     }
#     let a = 0;
#     let b = 0;
#     for (let i = 0; i < n; i++) {
#         if (mask & nums[i]) {
#             a ^= nums[i];
#         } else {
#             b ^= nums[i];
#         }
#     }
#     return [a, b];
# };