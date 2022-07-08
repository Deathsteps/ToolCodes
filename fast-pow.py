# https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

# FIXME: 快速幂
    def quickPow(self, x: int, n: int) -> int:
        if x == 0:
            return 0

        ret = 1
        negative = n < 0
        n = abs(n)

        while n:
            if n & 1:
                ret = self.quickMulti(ret, x)
            n >>= 1
            x = self.quickMulti(x, x)  # x = x * x 或者 x = x ^ 2
        return 1 / ret if negative else ret

  # FIXME: 快速乘
  # https://www.jianshu.com/p/b729afff99ef
  def quickMulti(self, x: int, b: int) -> int:
      ret = 0
      while b:
          if b & 1:
              ret += x
          b >>= 1
          x <<= 1  # x = x + x 或者 x = x * 2
      return ret
