class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        st = [0]

        for i in range(len(s)):

            if s[i] == "(":

                st.append(0)

            else:
                val = max(2*st.pop(), 1)

                st[-1] += val

        return st[-1]






        