class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sx = str(x)
        if '-' in sx:
            reversed_int = int('-' + sx[::-1].rstrip('-'))
        else:
            reversed_int = int(sx[::-1])

        if not (-2**31) < reversed_int < (2**31 - 1):
            reversed_int = 0

        return reversed_int


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-214748364))
