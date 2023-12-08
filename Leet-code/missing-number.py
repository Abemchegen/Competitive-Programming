class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
       total=sum(nums)
       n=len(nums)
       truetotal=(n*n + n)//2
       return truetotal - total



        