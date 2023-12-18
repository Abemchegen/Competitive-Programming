class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0, len(s), k * 2):
            sli = s[i:i + k]
            rev= sli[::-1]
            ans += rev + s[i + k:i + k * 2]
        return ans
