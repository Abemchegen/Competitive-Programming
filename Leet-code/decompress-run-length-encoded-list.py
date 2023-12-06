class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=1
        ans=[]
        while(i<len(nums)):
            ans+=[nums[i]]* nums[i-1]
            i+=2
        return ans
        