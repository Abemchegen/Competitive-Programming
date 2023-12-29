class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        n=Counter(nums)
        nums=list(set(nums))
        nums.sort()
        ans=0

        for i in range(len(nums)):
            ans+=n[nums[i]]*i
        return ans
        




        
        









        