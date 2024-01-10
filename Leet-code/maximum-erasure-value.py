class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        d=defaultdict(int)
        maxsum=0
        thissum=0
        left=0
        for i in range(len(nums)):
            d[nums[i]]+=1
            thissum+=nums[i]

            while d[nums[i]] > 1 :
                thissum-=nums[left]
                d[nums[left]]-=1
                left+=1
            maxsum=max(maxsum,thissum)

        return maxsum


        