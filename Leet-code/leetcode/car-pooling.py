class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        pre = [0] * 1001
        
        for i in range(len(trips)):

            pre[trips[i][1]] += trips[i][0]
            pre[trips[i][2]] -= trips[i][0]

        for i in range(1, len(pre)):

            pre[i] += pre[i-1]

        return max(pre) <= capacity








        