class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_substring = ''

        if len(strs) != 0:
            string_lengths = {len(s) for s in strs}
            shortest_length = min(string_lengths)

            if shortest_length > 0:
                if shortest_length == 1:
                    index_range = [1]
                else:
                    index_range = range(1, shortest_length + 1)

                for ending_index in index_range:
                    prefixes = {s[:ending_index] for s in strs}
                    if len(prefixes) == 1:
                        common_substring = prefixes.pop()
                    else:
                        break

        return common_substring


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(['abc', 'abd', 'abcd']))  # 'ab'
    print(s.longestCommonPrefix(['a']))  # 'a'
    print(s.longestCommonPrefix(['aa', 'aa']))  # 'aa'
