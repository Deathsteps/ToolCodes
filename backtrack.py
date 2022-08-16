# https://leetcode.cn/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/

# 39.组合总和

# 40. 组合总和 II

# 46. 全排列

# 47. 全排列 II

# 78. 子集

# 90. 子集 II

# 这类题目都是同一类型的,用回溯算法!

# 其实回溯算法关键在于:不合适就退回上一步

# 然后通过约束条件, 减少时间复杂度.

# 大家可以从下面的解法找出一点感觉!

# /**
#  * @param {number[]} nums
#  * @return {number[][]}
#  */
# var permute = function(nums, path) {
#     const n = nums.length;
#     let ret = [];
#     let used = new Set();
#     function dfs(k, path) {
#         if (k === n) {
#             ret.push(path);
#         } else {
#             for (let i = 0; i < n; i ++) {
#                 if (used.has(nums[i]))
#                     continue;
#                 // path.push(nums[i]);
#                 used.add(nums[i]);
#                 dfs(k + 1, path.concat(nums[i]));
#                 used.delete(nums[i]);
#                 // path.pop();
#             }
#         }
#     }
#     dfs(0, []);
#     return ret;
# };

# 什么时候使用 used 数组，什么时候使用 begin 变量
# 有些朋友可能会疑惑什么时候使用 used 数组，什么时候使用 begin 变量。这里为大家简单总结一下：

# 排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；
# 组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），需要按照某种顺序搜索，此时使用 begin 变量。

# 数组有重复就排序
# if j > begin and nums[j] == nums[j-1]: continue