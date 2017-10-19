class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numeral_to_int = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        number = 0
        previous_numeral_value = 0
        for c in reversed(s):
            value = numeral_to_int[c]
            if previous_numeral_value != 0:
                if previous_numeral_value <= value:
                    number += value
                else:
                    number -= value
            else:
                number = value
            previous_numeral_value = value

        return number


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("DCXXI"))  # 621
    print(s.romanToInt("MCMIV"))  # 1904