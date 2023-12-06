class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx=max(candies)
        ans=[]
        for i in candies:
            ans.append(i+extraCandies>=mx)
        return ans

        