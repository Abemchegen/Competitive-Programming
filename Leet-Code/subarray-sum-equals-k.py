class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        for i in range(1, len(nums)):
            nums[i]=nums[i] + nums[i-1]

        d=defaultdict(int)
        ans=0
        d[0]=1
     
        for i in range(len(nums)):

            if nums[i] - k in d :
                ans+=d[nums[i]-k]
            d[nums[i]]+=1

        print(d)
        return ans        