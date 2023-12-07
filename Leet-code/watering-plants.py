class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=len(plants)
        sum=0
        for i in range(len(plants)):
            sum+=plants[i]
            if sum>capacity:
                ans+= 2*i
                sum=plants[i]
        return ans

        
        