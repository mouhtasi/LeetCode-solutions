class Solution(object):
    from collections import deque
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 2:
            longest_substr = len(s)
        else:
            substr = Solution.deque()
            longest_substr = 0

            s += s[-1]
            for letter in s:
                if substr.count(letter):
                    substr_length = len(substr)
                    if substr_length > longest_substr:
                        longest_substr = substr_length
                    while substr.count(letter):
                        substr.popleft()

                substr.append(letter)

        return longest_substr




if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(s.lengthOfLongestSubstring('bbbbb'))  # 1
    print(s.lengthOfLongestSubstring('pwwkew'))  # 3
    print(s.lengthOfLongestSubstring('c'))  # 1
    print(s.lengthOfLongestSubstring('au'))  # 2
    print(s.lengthOfLongestSubstring("dvdf"))  # 3
