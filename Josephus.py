# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/

# 约瑟夫环问题

# 据说著名犹太历史学家Josephus有过以下的故事：在罗马人占领乔塔帕特后，39 个犹太人与Josephus及他的朋友躲到一个洞中，39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，
# 第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，直到所有人都自杀身亡为止。
# 然而Josephus 和他的朋友并不想遵从。首先从一个人开始，越过k-2个人（因为第一个人已经被越过），并杀掉第k个人。接着，再越过k-1个人，并杀掉第k个人。
# 这个过程沿着圆圈一直进行，直到最终只剩下一个人留下，这个人就可以继续活着。
# 问题是，给定了和，一开始要站在什么地方才能避免被处决。Josephus要他的朋友先假装遵从，他将朋友与自己安排在第16个与第31个位置，于是逃过了这场死亡游戏。

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # FIXME: 每杀掉一个人，其实就是把这个数组向前移动了 M 位。然后逆过来，就可以得到这个递推式。
        # fn = (fn-1 + m) % n
        # 假设 fn-1：[0, 1, 2, 3, 4]     m = 3
        #      fn：  [3, 4, 5, 0, 1, 2]  n = 5
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
