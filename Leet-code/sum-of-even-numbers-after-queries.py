class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum=0
        for i in nums:
            if i%2==0:
                sum+=i
        ans=[]
        for a, b in queries:
            if nums[b]%2==0:
                sum-=nums[b]
            nums[b]+=a
            
            if nums[b]%2==0:
                sum+=nums[b]
            ans.append(sum)
            
        return ans
      

        