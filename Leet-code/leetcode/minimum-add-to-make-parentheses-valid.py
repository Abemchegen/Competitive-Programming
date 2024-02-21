class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0
        op = 0
        for i in range(len(s)):

            if s[i] == "(" :

                op += 1

            elif op == 0:

                ans += 1

            else:

                op -= 1


        


        return ans + op
        