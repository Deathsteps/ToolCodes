# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/

# FIXME: 桶排序变种，原地哈希算法
# 主要应用在范围为 [0, len(nums)] 的数组解法中，将数组元素本身作为 nums 的下标，即 nums[nums[i]]
# 要求时间复杂度达到O(n)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        # 把 num 放到它该放的地方
        # 相同数处理
        # 方法一：取反
        # 方法二：增加偏移量
        for i in range(len(nums)):
            x = abs(nums[i])
            # 负数表明该位置已经放了元素
            # 偏移量类似，只不过负数处理变成 + 一个超大的偏移以超出 [1，n] 范围
            if nums[x - 1] < 0:
                ret.append(x)
            else:
                # 标记该位置有对应的元素
                nums[x - 1] = -nums[x - 1]

        return ret
