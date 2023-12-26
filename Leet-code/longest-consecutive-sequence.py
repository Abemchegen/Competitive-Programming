class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)<1:
            return 0
            
        nums.sort()

        count=1
        ans=0

        for i in range(1,len(nums)):

            if nums[i]==nums[i-1]+1 :
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                ans=max(count,ans)
                count=1
        ans=max(ans,count)
        return ans

