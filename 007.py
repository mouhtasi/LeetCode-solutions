class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = (x > 0) - (x < 0)  # 1 for positive, 0 for 0, -1 for negative
        reversed_int = int(str(abs(x))[::-1])
        if not reversed_int < (2**31 - 1):
            reversed_int = 0

        return sign * reversed_int


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-214748364))
