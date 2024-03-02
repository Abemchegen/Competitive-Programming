class Solution:
    def bestClosingTime(self, customers: str) -> int:


        pre = [0] * (len(customers) + 1)

        for i in range(len(customers)):

            if customers[i] == "Y":
                pre[i + 1] = 1

        for i in range(1, len(pre)):
            pre[i] += pre[i-1]

        ans = []
        count = 0

        for i in range(1, len(pre)):

            ans.append(pre[-1] - pre[i-1] + count)
            
            if pre[i] == pre[i-1]:
                count += 1

        ans.append(len(customers) - pre[-1] )

        return ans.index(min(ans))
        







