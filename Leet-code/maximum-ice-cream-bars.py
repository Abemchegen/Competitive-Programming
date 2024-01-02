class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        countingsort=[0]*max(costs)

        for i in range(len(costs)):
            countingsort[costs[i]-1]+=1
        costs=[]
        for i in range(len(countingsort)):
            costs.extend([i+1] * countingsort[i])
        total=0
        ans=0
        print(costs)
        for i in range(len(costs)):
            total+=costs[i]
            if total<coins:
                ans+=1
            elif total==coins:
                ans+=1
                break
            elif total>coins:
                break
        return ans


        


        