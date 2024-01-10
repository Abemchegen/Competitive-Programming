class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        
        total=sum(nums[:k])
        maxave=total/k
        left=0
        for i in range(k,len(nums)):
            total-=nums[left]
            left+=1
            total+=nums[i]
            maxave=max(maxave, total/k)
        return maxave


        