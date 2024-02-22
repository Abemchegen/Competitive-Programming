class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        for i in range(len(s)):

            if s[i] == "{" or s[i] == "[" or s[i] == "(" :

                st.append(s[i])

            elif len(st) != 0 and ((s[i] == "}" and st[-1] == "{" ) or (s[i] == ")" and st[-1] == "(") or (s[i] == "]" and st[-1] == "[") ):

                    st.pop()
            else:
                return False

        return len(st) == 0

        