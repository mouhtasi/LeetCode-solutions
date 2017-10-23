class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid = True

        left_brackets = ['(', '{', '[']
        matching_brackets = {'(': ')', '{': '}', '[': ']'}

        opening_brackets = []

        for bracket in s:
            if bracket in left_brackets:
                opening_brackets.append(bracket)
            else:  # closing bracket
                if opening_brackets and matching_brackets[opening_brackets[-1:][0]] == bracket:
                    opening_brackets.pop()
                else:
                    valid = False
                    break

        if len(opening_brackets) != 0:
            valid = False

        return valid


if __name__ == "__main__":
    s = Solution()
    print(s.isValid('()'))  # True
    print(s.isValid('(}'))  # False
    print(s.isValid('({[]})'))  # True
    print(s.isValid('([[}})'))  # False
    print(s.isValid('()[]{}'))  # True
    print(s.isValid(']'))  # False
