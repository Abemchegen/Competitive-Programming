class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        let = set(s)

        for i in range(len(s)):

            if s[i].swapcase() not in let:

                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) < len(right):
                    return right
                else:
                    return left
        return s
        