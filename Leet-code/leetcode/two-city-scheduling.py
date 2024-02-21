class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x : -abs(x[0] - x[1]))
        

        A = B = len(costs) // 2

        total = 0

        for a , b in costs :

            if A == 0 or (B > 0 and b <= a) :    

                B -= 1
                total += b

            else:

                A -= 1
                total += a

        return total  

