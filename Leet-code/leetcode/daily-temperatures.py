class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while len(st) > 0 and temperatures[i] > temperatures[st[-1]]  :

                ans[st[-1]] = i - st[-1]
                st.pop()

            st.append(i) 

        return ans
        