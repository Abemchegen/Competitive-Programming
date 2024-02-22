class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []


        for i in range(len(tokens)):

            if tokens[i] == '*' or tokens[i] == '/' or tokens[i] == '+' or tokens[i] == '-':
               
                a = int(st[-1])
                st.pop()
                b = int(st[-1])
                st.pop()

          
                if tokens[i] == '*' :

                    st.append(a * b)

                elif tokens[i] == '+' :

                    st.append(a + b)

                elif tokens[i] == '-' :

                    st.append(b - a)

                else:
                    st.append(int(b/a))
            else:
                st.append(tokens[i])

        return int(st[-1])
        