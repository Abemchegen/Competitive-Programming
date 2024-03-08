class Solution:
    def decodeString(self, s: str) -> str:

        st = []
        ans = []

        for i in range(len(s)):
            if s[i] == "]":
                
                while s[i] == "]" and st[-1] != "[" :

                    ans.append(st.pop())
                st.pop()
                ans.reverse()
                ans = "".join(ans)

                num = []
                while st and st[-1].isdigit() :

                    num.append(st.pop())
                num.reverse()
                num = "".join(num)
                num = int(num)
                ans *= num
                st.append(ans)
                ans = []
            else:

                st.append(s[i])
        st = "".join(st)
        return st

        
        